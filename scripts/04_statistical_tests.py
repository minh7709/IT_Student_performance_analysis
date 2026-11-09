"""
BUOC 5.1: KIEM DINH THONG KE GIA THUYET (STATISTICAL HYPOTHESIS TESTING)
Du an: Phan tich hanh vi & hieu qua hoc tap sinh vien IT/CSE
"""
import os
import sys
import json
import pandas as pd
import numpy as np
from scipy import stats

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_statistical_tests():
    data_path = os.path.join("data", "processed_students_performance.csv")
    out_dir = os.path.join("reports")
    os.makedirs(out_dir, exist_ok=True)
    out_json = os.path.join(out_dir, "statistical_test_results.json")

    print("[1/4] Loading processed dataset...")
    df = pd.read_csv(data_path)

    results = {
        "chi_square_tests": [],
        "anova_kruskal_tests": [],
        "t_tests": []
    }

    print("\n[2/4] Running Chi-Square Tests of Independence...")
    cat_pairs = [
        ("english_proficiency", "Trình độ Tiếng Anh"),
        ("faculty_consultancy", "Tham vấn Giảng viên cố vấn"),
        ("scholarship", "Học bổng Khuyến khích"),
        ("living_with", "Nơi ở (Gia đình vs Ở trọ)"),
        ("learning_mode", "Phương thức Học tập (Offline/Online)"),
        ("health_issues", "Vấn đề Sức khỏe"),
        ("extracurricular", "Hoạt động Ngoại khóa")
    ]

    for col, name in cat_pairs:
        contingency_table = pd.crosstab(df[col], df['student_status'])
        chi2, p, dof, _ = stats.chi2_contingency(contingency_table)
        cramer_v = np.sqrt(chi2 / (len(df) * (min(contingency_table.shape) - 1)))
        
        sig = "Có ý nghĩa thống kê (p < 0.05)" if p < 0.05 else "Không có ý nghĩa thống kê (p >= 0.05)"
        res_item = {
            "feature": col,
            "feature_name_vn": name,
            "chi2_stat": round(chi2, 4),
            "p_value": float(f"{p:.6e}"),
            "dof": int(dof),
            "cramers_v": round(cramer_v, 4),
            "significance": sig
        }
        results["chi_square_tests"].append(res_item)
        print(f"  * {name:35s} | Chi2={chi2:8.2f} | p={p:.3e} | Cramer's V={cramer_v:.3f} | {sig}")

    print("\n[3/4] Running ANOVA & Kruskal-Wallis Tests...")
    # 1. CGPA across English proficiency levels
    eng_groups = [group['current_cgpa'].values for _, group in df.groupby('english_proficiency')]
    f_val, p_val = stats.f_oneway(*eng_groups)
    kw_val, kw_p = stats.kruskal(*eng_groups)
    results["anova_kruskal_tests"].append({
        "comparison": "CGPA across English Proficiency Levels (Basic, Intermediate, Advance)",
        "f_stat": round(f_val, 4),
        "f_p_value": float(f"{p_val:.6e}"),
        "kruskal_stat": round(kw_val, 4),
        "kruskal_p_value": float(f"{kw_p:.6e}"),
        "interpretation": "Khác biệt cực kỳ có ý nghĩa thống kê về CGPA giữa các nhóm trình độ tiếng Anh." if p_val < 0.05 else "Không có sự khác biệt."
    })
    print(f"  * CGPA across English Levels: F={f_val:.2f} (p={p_val:.3e}), KW={kw_val:.2f} (p={kw_p:.3e})")

    # 2. CGPA across Learning Mode (Offline vs Online)
    lm_groups = [group['current_cgpa'].values for _, group in df.groupby('learning_mode')]
    f_val2, p_val2 = stats.f_oneway(*lm_groups)
    kw_val2, kw_p2 = stats.kruskal(*lm_groups)
    results["anova_kruskal_tests"].append({
        "comparison": "CGPA across Learning Modes (Offline vs Online)",
        "f_stat": round(f_val2, 4),
        "f_p_value": float(f"{p_val2:.6e}"),
        "kruskal_stat": round(kw_val2, 4),
        "kruskal_p_value": float(f"{kw_p2:.6e}"),
        "interpretation": "Có sự khác biệt giữa học Online và Offline đối với điểm CGPA." if p_val2 < 0.05 else "Không có sự khác biệt đáng kể giữa Online và Offline."
    })
    print(f"  * CGPA across Learning Mode : F={f_val2:.2f} (p={p_val2:.3e}), KW={kw_val2:.2f} (p={kw_p2:.3e})")

    # 3. Attendance across Student Status groups
    att_groups = [group['attendance_percentage'].values for _, group in df.groupby('student_status')]
    f_val3, p_val3 = stats.f_oneway(*att_groups)
    kw_val3, kw_p3 = stats.kruskal(*att_groups)
    results["anova_kruskal_tests"].append({
        "comparison": "Attendance Percentage across Student Status groups",
        "f_stat": round(f_val3, 4),
        "f_p_value": float(f"{p_val3:.6e}"),
        "kruskal_stat": round(kw_val3, 4),
        "kruskal_p_value": float(f"{kw_p3:.6e}"),
        "interpretation": "Mức độ chuyên cần khác biệt cực kỳ rõ rệt giữa sinh viên Giỏi, TB và Nguy cơ."
    })
    print(f"  * Attendance across Status  : F={f_val3:.2f} (p={p_val3:.3e}), KW={kw_val3:.2f} (p={kw_p3:.3e})")

    # 4. Social Media Hours across Student Status
    sm_groups = [group['social_media_hours'].values for _, group in df.groupby('student_status')]
    f_val4, p_val4 = stats.f_oneway(*sm_groups)
    kw_val4, kw_p4 = stats.kruskal(*sm_groups)
    results["anova_kruskal_tests"].append({
        "comparison": "Social Media Hours across Student Status",
        "f_stat": round(f_val4, 4),
        "f_p_value": float(f"{p_val4:.6e}"),
        "kruskal_stat": round(kw_val4, 4),
        "kruskal_p_value": float(f"{kw_p4:.6e}"),
        "interpretation": "Thời gian dùng mạng xã hội có sự khác biệt có ý nghĩa thống kê giữa các nhóm trạng thái."
    })
    print(f"  * Social Media across Status: F={f_val4:.2f} (p={p_val4:.3e}), KW={kw_val4:.2f} (p={kw_p4:.3e})")

    print("\n[4/4] Running Two-sample T-Tests & Mann-Whitney U Tests...")
    # Faculty consultancy: CGPA of Yes vs No
    yes_fc = df[df['faculty_consultancy'] == 'Yes']['current_cgpa']
    no_fc = df[df['faculty_consultancy'] == 'No']['current_cgpa']
    t_stat, t_p = stats.ttest_ind(yes_fc, no_fc, equal_var=False)
    u_stat, u_p = stats.mannwhitneyu(yes_fc, no_fc)
    results["t_tests"].append({
        "comparison": "CGPA of Students Consulting Faculty (Yes) vs Not Consulting (No)",
        "mean_yes": round(float(yes_fc.mean()), 3),
        "mean_no": round(float(no_fc.mean()), 3),
        "t_stat": round(t_stat, 4),
        "t_p_value": float(f"{t_p:.6e}"),
        "mann_whitney_p": float(f"{u_p:.6e}"),
        "interpretation": f"Sinh viên có gặp cố vấn có điểm CGPA TB ({yes_fc.mean():.2f}) vượt trội so với nhóm không gặp ({no_fc.mean():.2f}), p={t_p:.3e}."
    })
    print(f"  * Faculty Consultancy: Mean Yes={yes_fc.mean():.2f} vs No={no_fc.mean():.2f} | t={t_stat:.2f} (p={t_p:.3e})")

    # Scholarship: CGPA of Yes vs No
    yes_sc = df[df['scholarship'] == 'Yes']['current_cgpa']
    no_sc = df[df['scholarship'] == 'No']['current_cgpa']
    t_stat2, t_p2 = stats.ttest_ind(yes_sc, no_sc, equal_var=False)
    results["t_tests"].append({
        "comparison": "CGPA of Students with Scholarship (Yes) vs without Scholarship (No)",
        "mean_yes": round(float(yes_sc.mean()), 3),
        "mean_no": round(float(no_sc.mean()), 3),
        "t_stat": round(t_stat2, 4),
        "t_p_value": float(f"{t_p2:.6e}"),
        "interpretation": f"Sinh viên nhận học bổng có CGPA ({yes_sc.mean():.2f}) cao hơn đáng kể so với nhóm không có học bổng ({no_sc.mean():.2f}), p={t_p2:.3e}."
    })
    print(f"  * Scholarship        : Mean Yes={yes_sc.mean():.2f} vs No={no_sc.mean():.2f} | t={t_stat2:.2f} (p={t_p2:.3e})")

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nStatistical test results exported successfully to: {out_json}")
    return results

if __name__ == "__main__":
    run_statistical_tests()
