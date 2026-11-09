"""
BUOC 4: TRUC QUAN HOA DU LIEU & PHAN TICH KHAM PHA (EDA)
Du an: Phan tich hanh vi & hieu qua hoc tap sinh vien IT/CSE
"""
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def generate_visualizations():
    # Setup aesthetic theme
    sns.set_theme(style="whitegrid", font="sans-serif")
    palette_status = {"Good Standing": "#2ecc71", "Average Standing": "#3498db", "Academic Risk": "#e74c3c"}
    
    data_path = os.path.join("data", "processed_students_performance.csv")
    fig_dir = os.path.join("reports", "figures")
    os.makedirs(fig_dir, exist_ok=True)
    
    print("[1/10] Loading processed dataset...")
    df = pd.read_csv(data_path)

    # ----------------------------------------------------
    # BIỂU ĐỒ 1: Tương quan Giờ học & Mạng xã hội theo Trạng thái học tập
    # ----------------------------------------------------
    print("[2/10] Generating Figure 1: Study vs Social Media Scatter Plot...")
    plt.figure(figsize=(9, 6), dpi=300)
    sns.scatterplot(
        data=df,
        x="social_media_hours",
        y="daily_study_hours",
        hue="student_status",
        palette=palette_status,
        alpha=0.65,
        s=50,
        edgecolor='w',
        linewidth=0.5
    )
    # Fit regression trendline for overall trend
    sns.regplot(
        data=df,
        x="social_media_hours",
        y="daily_study_hours",
        scatter=False,
        color="#2c3e50",
        line_kws={"linestyle": "--", "linewidth": 2, "label": "Xu hướng chung"}
    )
    plt.title("Hành vi Tự học vs Thời gian Dùng Mạng xã hội theo Phân loại Sinh viên", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Thời gian dùng Mạng xã hội mỗi ngày (Giờ)", fontsize=11)
    plt.ylabel("Thời gian Tự học mỗi ngày (Giờ)", fontsize=11)
    plt.legend(title="Trạng thái sinh viên", frameon=True, loc="upper right")
    plt.tight_layout()
    f1_path = os.path.join(fig_dir, "01_study_vs_social_media.png")
    plt.savefig(f1_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 2: Tác động của Chuyên cần (Attendance Percentage)
    # ----------------------------------------------------
    print("[3/10] Generating Figure 2: Attendance Violin & Box Plot...")
    plt.figure(figsize=(9, 6), dpi=300)
    sns.violinplot(
        data=df,
        x="student_status",
        y="attendance_percentage",
        order=["Good Standing", "Average Standing", "Academic Risk"],
        palette=palette_status,
        inner="quartile",
        cut=0,
        linewidth=1.5
    )
    # Add horizontal threshold line at 80%
    plt.axhline(80, color='red', linestyle='--', linewidth=1.5, label='Ngưỡng chuyên cần chuẩn (80%)')
    plt.title("Phân phối Mức độ Chuyên cần (%) theo Trạng thái Học tập", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Trạng thái Sinh viên (Student Status)", fontsize=11)
    plt.ylabel("Tỷ lệ Chuyên cần (%)", fontsize=11)
    plt.legend(loc="lower left", frameon=True)
    plt.tight_layout()
    f2_path = os.path.join(fig_dir, "02_attendance_distribution.png")
    plt.savefig(f2_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 3: Trình độ Tiếng Anh vs Điểm CGPA
    # ----------------------------------------------------
    print("[4/10] Generating Figure 3: English Skills vs CGPA...")
    plt.figure(figsize=(8, 6), dpi=300)
    order_eng = ["Basic", "Intermediate", "Advance"]
    sns.boxplot(
        data=df,
        x="english_proficiency",
        y="current_cgpa",
        order=order_eng,
        palette=["#e67e22", "#3498db", "#2ecc71"],
        boxprops=dict(alpha=0.75),
        showmeans=True,
        meanprops={"marker": "D", "markerfacecolor": "red", "markeredgecolor": "red", "markersize": "7"}
    )
    plt.title("Tác động của Trình độ Tiếng Anh đến Điểm Tích lũy (CGPA)", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Trình độ Tiếng Anh (English Proficiency)", fontsize=11)
    plt.ylabel("Điểm Tích lũy Hiện tại (CGPA thang 4.0)", fontsize=11)
    plt.tight_layout()
    f3_path = os.path.join(fig_dir, "03_english_vs_cgpa.png")
    plt.savefig(f3_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 4: Yếu tố Rủi ro Học vụ (Probation & Suspension)
    # ----------------------------------------------------
    print("[5/10] Generating Figure 4: Academic Risk Stacked Bar Chart...")
    prob_ct = pd.crosstab(df['probation'], df['student_status'], normalize='index') * 100
    prob_ct = prob_ct[['Good Standing', 'Average Standing', 'Academic Risk']]
    
    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    prob_ct.plot(
        kind='bar',
        stacked=True,
        color=["#2ecc71", "#3498db", "#e74c3c"],
        ax=ax,
        edgecolor='white',
        linewidth=1
    )
    plt.title("Tỷ lệ Phân bổ Trạng thái Học tập theo Tiền sử Cảnh cáo Học vụ (Probation)", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Từng bị Cảnh cáo Học vụ (Probation)?", fontsize=11)
    plt.ylabel("Tỷ lệ phần trăm (%)", fontsize=11)
    plt.xticks(ticks=[0, 1], labels=["Chưa từng (No)", "Đã từng bị cảnh cáo (Yes)"], rotation=0)
    plt.legend(title="Trạng thái sinh viên", bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    f4_path = os.path.join(fig_dir, "04_probation_vs_status.png")
    plt.savefig(f4_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 5: Môi trường sống, Sức khỏe & Giờ tự học
    # ----------------------------------------------------
    print("[6/10] Generating Figure 5: Living Status & Health vs Study Hours...")
    plt.figure(figsize=(9, 5), dpi=300)
    sns.barplot(
        data=df,
        x="living_with",
        y="daily_study_hours",
        hue="health_issues",
        palette={"No": "#3498db", "Yes": "#e67e22"},
        errorbar=('ci', 95),
        capsize=0.1
    )
    plt.title("Thời gian Tự học trung bình theo Môi trường sống & Vấn đề Sức khỏe", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Môi trường Sống (Ở với Gia đình vs Ở trọ/Bachelor)", fontsize=11)
    plt.ylabel("Giờ tự học mỗi ngày (kèm khoảng tin cậy 95%)", fontsize=11)
    plt.legend(title="Có vấn đề sức khỏe?", loc="upper right")
    plt.tight_layout()
    f5_path = os.path.join(fig_dir, "05_living_health_study.png")
    plt.savefig(f5_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 6: Hiệu quả của Tư vấn từ Giảng viên (Faculty Consultancy)
    # ----------------------------------------------------
    print("[7/10] Generating Figure 6: Faculty Consultancy KDE Plot...")
    plt.figure(figsize=(9, 5.5), dpi=300)
    sns.kdeplot(
        data=df[df['faculty_consultancy'] == 'Yes'],
        x="current_cgpa",
        fill=True,
        color="#2980b9",
        label="Có tham vấn giảng viên (Yes)",
        alpha=0.4,
        linewidth=2
    )
    sns.kdeplot(
        data=df[df['faculty_consultancy'] == 'No'],
        x="current_cgpa",
        fill=True,
        color="#e74c3c",
        label="Không tham vấn giảng viên (No)",
        alpha=0.4,
        linewidth=2
    )
    plt.axvline(df[df['faculty_consultancy'] == 'Yes']['current_cgpa'].mean(), color='#2980b9', linestyle=':', label=f"TB Nhóm Có: {df[df['faculty_consultancy'] == 'Yes']['current_cgpa'].mean():.2f}")
    plt.axvline(df[df['faculty_consultancy'] == 'No']['current_cgpa'].mean(), color='#e74c3c', linestyle=':', label=f"TB Nhóm Không: {df[df['faculty_consultancy'] == 'No']['current_cgpa'].mean():.2f}")
    plt.title("Phân phối Mật độ CGPA: So sánh Sinh viên Có và Không Tham vấn Giảng viên", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Điểm Tích lũy (CGPA)", fontsize=11)
    plt.ylabel("Mật độ phân phối (Density)", fontsize=11)
    plt.legend(loc="upper left")
    plt.tight_layout()
    f6_path = os.path.join(fig_dir, "06_faculty_consultancy_impact.png")
    plt.savefig(f6_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 7: Phân phối Biến Mục Tiêu (Target Class Distribution)
    # ----------------------------------------------------
    print("[8/10] Generating Figure 7: Target Status Distribution...")
    plt.figure(figsize=(7, 5), dpi=300)
    status_order = ["Good Standing", "Average Standing", "Academic Risk"]
    counts = df['student_status'].value_counts()[status_order]
    pcts = (counts / len(df)) * 100
    bars = plt.bar(status_order, counts, color=["#2ecc71", "#3498db", "#e74c3c"], width=0.6, edgecolor='gray', alpha=0.85)
    for bar, pct in zip(bars, pcts):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f"{int(yval)} ({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=10)
    plt.title("Phân bổ Số lượng và Tỷ lệ của Biến Mục tiêu (Student Status)", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Trạng thái Học tập", fontsize=11)
    plt.ylabel("Số lượng Sinh viên", fontsize=11)
    plt.ylim(0, max(counts) * 1.15)
    plt.tight_layout()
    f7_path = os.path.join(fig_dir, "07_target_status_distribution.png")
    plt.savefig(f7_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 8: Ma trận Tương quan (Correlation Heatmap)
    # ----------------------------------------------------
    print("[9/10] Generating Figure 8: Correlation Matrix Heatmap...")
    corr_cols = [
        "current_cgpa", "previous_sgpa", "attendance_percentage",
        "daily_study_hours", "social_media_hours", "study_to_social_ratio",
        "study_effort_index", "academic_risk_score", "academic_support_index",
        "credits_completed", "age"
    ]
    corr_labels = [
        "CGPA", "SGPA", "Chuyên cần (%)",
        "Giờ tự học", "Giờ dùng MXH", "Tỷ lệ Học/MXH",
        "Chỉ số nỗ lực", "Điểm rủi ro", "Hỗ trợ học vụ",
        "Tín chỉ đạt", "Tuổi"
    ]
    corr_matrix = df[corr_cols].corr()
    
    plt.figure(figsize=(10, 8), dpi=300)
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-0.6,
        vmax=0.8,
        xticklabels=corr_labels,
        yticklabels=corr_labels,
        linewidths=0.5,
        cbar_kws={'label': 'Hệ số tương quan Pearson (r)'}
    )
    plt.title("Ma trận Tương quan Tuyến tính giữa các Biến Số Học tập & Hành vi", fontsize=13, fontweight='bold', pad=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    f8_path = os.path.join(fig_dir, "08_correlation_matrix.png")
    plt.savefig(f8_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 9: Phân tích Kỹ năng IT hàng đầu (Top CSE Skills)
    # ----------------------------------------------------
    print("[10/10] Generating Figure 9: Top CSE Skills Distribution...")
    plt.figure(figsize=(9, 5), dpi=300)
    top_skills = df['skills'].value_counts().head(7)
    sns.barplot(
        x=top_skills.values,
        y=top_skills.index,
        palette="viridis",
        edgecolor='w'
    )
    for i, v in enumerate(top_skills.values):
        plt.text(v + 5, i, f"{v} ({v/len(df)*100:.1f}%)", va='center', fontweight='bold', fontsize=9.5)
    plt.title("Phân bố Kỹ năng Công nghệ Nổi bật của Sinh viên CSE", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Số lượng Sinh viên", fontsize=11)
    plt.ylabel("Kỹ năng Công nghệ (Skills)", fontsize=11)
    plt.xlim(0, max(top_skills.values) * 1.15)
    plt.tight_layout()
    f9_path = os.path.join(fig_dir, "09_top_cse_skills.png")
    plt.savefig(f9_path, dpi=300)
    plt.close()

    print(f"\nAll 9 professional figures successfully generated in: {fig_dir}")

if __name__ == "__main__":
    generate_visualizations()
