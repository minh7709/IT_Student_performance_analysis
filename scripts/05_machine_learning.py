"""
BUOC 5.2: HUAN LUYEN MO HINH MACHINE LEARNING & TRICH XUAT FEATURE IMPORTANCE
Du an: Phan tich hanh vi & hieu qua hoc tap sinh vien IT/CSE
"""
import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def train_and_evaluate_models():
    data_path = os.path.join("data", "processed_students_performance.csv")
    fig_dir = os.path.join("reports", "figures")
    out_json = os.path.join("reports", "model_evaluation_results.json")
    os.makedirs(fig_dir, exist_ok=True)

    print("[1/6] Loading processed data...")
    df = pd.read_csv(data_path)

    # Define feature set: Predict Student Status using Behavioral & Academic Factors
    # To avoid data leakage from the direct definition of student_status,
    # we exclude: current_cgpa, probation, suspension, academic_risk_score, gpa_progression
    target_col = "student_status"
    y = df[target_col]

    feature_cols = [
        # Numerical
        "attendance_percentage", "daily_study_hours", "study_frequency",
        "social_media_hours", "study_to_social_ratio", "study_effort_index",
        "academic_support_index", "previous_sgpa", "credits_completed",
        "monthly_income", "gap_year", "age", "current_semester",
        # Categorical
        "gender", "learning_mode", "english_proficiency", "scholarship",
        "faculty_consultancy", "university_transport", "extracurricular",
        "living_with", "health_issues", "physical_disabilities", "relationship_status"
    ]
    X = df[feature_cols]

    num_features = [
        "attendance_percentage", "daily_study_hours", "study_frequency",
        "social_media_hours", "study_to_social_ratio", "study_effort_index",
        "academic_support_index", "previous_sgpa", "credits_completed",
        "monthly_income", "gap_year", "age", "current_semester"
    ]
    cat_features = [
        "gender", "learning_mode", "english_proficiency", "scholarship",
        "faculty_consultancy", "university_transport", "extracurricular",
        "living_with", "health_issues", "physical_disabilities", "relationship_status"
    ]

    print(f"Total features: {len(feature_cols)} ({len(num_features)} numerical, {len(cat_features)} categorical)")

    # Preprocessor pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_features),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_features)
        ]
    )

    # Models dictionary
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=4, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(n_estimators=150, learning_rate=0.08, max_depth=4, random_state=42)
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scoring = ['accuracy', 'f1_macro', 'f1_weighted']

    print("\n[2/6] Running 5-Fold Stratified Cross-Validation on Models...")
    cv_results = {}
    for name, model in models.items():
        pipe = Pipeline(steps=[('prep', preprocessor), ('clf', model)])
        scores = cross_validate(pipe, X, y, cv=cv, scoring=scoring, n_jobs=-1)
        cv_results[name] = {
            "accuracy_mean": round(float(scores['test_accuracy'].mean()), 4),
            "accuracy_std": round(float(scores['test_accuracy'].std()), 4),
            "f1_macro_mean": round(float(scores['test_f1_macro'].mean()), 4),
            "f1_macro_std": round(float(scores['test_f1_macro'].std()), 4),
            "f1_weighted_mean": round(float(scores['test_f1_weighted'].mean()), 4),
            "f1_weighted_std": round(float(scores['test_f1_weighted'].std()), 4)
        }
        print(f"  * {name:20s}: Accuracy={cv_results[name]['accuracy_mean']:.3f} (+/- {cv_results[name]['accuracy_std']:.3f}) | F1-Macro={cv_results[name]['f1_macro_mean']:.3f}")

    # ---- AUTO-SELECT best model by F1-Weighted (CV) ----
    best_name = max(cv_results, key=lambda k: cv_results[k]['f1_weighted_mean'])
    print(f"\n  >>> Best model (by F1-Weighted CV): [{best_name}]")
    print(f"      F1-Weighted = {cv_results[best_name]['f1_weighted_mean']:.4f} | Accuracy = {cv_results[best_name]['accuracy_mean']:.4f}")

    # Train / Test split for detailed diagnostics & confusion matrix
    print(f"\n[3/6] Fitting Best Model [{best_name}] on Train/Test Split (80/20)...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    best_pipe = Pipeline(steps=[('prep', preprocessor), ('clf', models[best_name])])
    best_pipe.fit(X_train, y_train)
    y_pred = best_pipe.predict(X_test)

    acc_test = accuracy_score(y_test, y_pred)
    f1_macro_test = f1_score(y_test, y_pred, average='macro')
    cls_report = classification_report(y_test, y_pred, output_dict=True)
    
    print(f"Test Accuracy: {acc_test:.4f} | Test F1-Macro: {f1_macro_test:.4f}")

    # ----------------------------------------------------
    # BIỂU ĐỒ 10: Ma trận Nhầm lẫn (Confusion Matrix)
    # ----------------------------------------------------
    print("[4/6] Generating Figure 10: Confusion Matrix...")
    classes = ["Good Standing", "Average Standing", "Academic Risk"]
    cm = confusion_matrix(y_test, y_pred, labels=classes)
    cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.figure(figsize=(7, 6), dpi=300)
    sns.heatmap(
        cm_norm,
        annot=True,
        fmt=".2%",
        cmap="Blues",
        xticklabels=classes,
        yticklabels=classes,
        cbar=True,
        linewidths=1
    )
    plt.title(f"Ma trận Nhầm lẫn (Confusion Matrix) - {best_name} (Độ chính xác: {acc_test:.1%})", fontsize=12, fontweight='bold', pad=12)
    plt.xlabel("Trạng thái Dự đoán (Predicted)", fontsize=11)
    plt.ylabel("Trạng thái Thực tế (True)", fontsize=11)
    plt.tight_layout()
    f10_path = os.path.join(fig_dir, "10_confusion_matrix.png")
    plt.savefig(f10_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # BIỂU ĐỒ 11: Tầm quan trọng Đặc trưng (Feature Importance)
    # ----------------------------------------------------
    print("[5/6] Extracting Feature Importance & Generating Figure 11...")
    # Get encoded feature names
    cat_encoder = best_pipe.named_steps['prep'].named_transformers_['cat']
    encoded_cat_names = cat_encoder.get_feature_names_out(cat_features).tolist()
    all_feature_names = num_features + encoded_cat_names

    best_model = best_pipe.named_steps['clf']

    # Tree-based models → feature_importances_; Logistic Regression → |coef_|
    if hasattr(best_model, 'feature_importances_'):
        importances = best_model.feature_importances_
        importance_label = "Mức độ Quan trọng Tương đối (Gini Importance)"
    else:
        importances = np.abs(best_model.coef_).mean(axis=0)
        importance_label = "Mức độ Quan trọng Tương đối (|Coef| trung bình)"

    fi_df = pd.DataFrame({
        "Feature": all_feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False)

    # Map friendly names for top features
    friendly_names = {
        "attendance_percentage": "Tỷ lệ Chuyên cần (%)",
        "previous_sgpa": "Điểm Học kỳ trước (SGPA)",
        "study_effort_index": "Chỉ số Nỗ lực Học tập",
        "credits_completed": "Số Tín chỉ đã Hoàn thành",
        "study_to_social_ratio": "Tỷ lệ Học / Dùng MXH",
        "daily_study_hours": "Thời gian Tự học mỗi ngày",
        "social_media_hours": "Thời gian Dùng MXH mỗi ngày",
        "monthly_income": "Thu nhập Gia đình mỗi tháng",
        "academic_support_index": "Chỉ số Hỗ trợ Học vụ",
        "scholarship_Yes": "Có Học bổng Khuyến khích",
        "scholarship_No": "Không có Học bổng",
        "age": "Độ tuổi Sinh viên",
        "study_frequency": "Số lần Ngồi vào bàn học",
        "current_semester": "Học kỳ Hiện tại",
        "gap_year": "Số năm Gián đoạn trước ĐH"
    }
    fi_df["Feature_VN"] = fi_df["Feature"].map(lambda x: friendly_names.get(x, x))
    top_12 = fi_df.head(12)

    plt.figure(figsize=(9, 6), dpi=300)
    sns.barplot(
        data=top_12,
        x="Importance",
        y="Feature_VN",
        hue="Feature_VN",
        palette="crest",
        legend=False,
        edgecolor='w'
    )
    for i, v in enumerate(top_12['Importance'].values):
        plt.text(v + 0.002, i, f"{v:.3f} ({v*100:.1f}%)", va='center', fontweight='bold', fontsize=9.5)
    plt.title(f"Top 12 Đặc trưng Tác động Lớn nhất đến Trạng thái Học tập ({best_name})", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel(importance_label, fontsize=11)
    plt.ylabel("Đặc trưng (Feature)", fontsize=11)
    plt.xlim(0, max(top_12['Importance']) * 1.18)
    plt.tight_layout()
    f11_path = os.path.join(fig_dir, "11_feature_importance.png")
    plt.savefig(f11_path, dpi=300)
    plt.close()

    # ----------------------------------------------------
    # Lưu toàn bộ báo cáo kết quả ML ra JSON
    # ----------------------------------------------------
    print("[6/6] Saving ML experiment artifacts...")
    final_output = {
        "best_model_selected": best_name,
        "best_model_cv_f1_weighted": cv_results[best_name]['f1_weighted_mean'],
        "cross_validation_results": cv_results,
        "test_set_evaluation": {
            "model": best_name,
            "accuracy": round(float(acc_test), 4),
            "f1_macro": round(float(f1_macro_test), 4),
            "classification_report": cls_report
        },
        "top_features": top_12[["Feature", "Feature_VN", "Importance"]].to_dict(orient="records")
    }

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)

    print(f"\nModel training and evaluation successfully finished! Results in: {out_json}")
    print(f"  Best model auto-selected: [{best_name}] | F1-Weighted={cv_results[best_name]['f1_weighted_mean']:.4f} | Test Acc={acc_test:.4f}")
    return final_output

if __name__ == "__main__":
    train_and_evaluate_models()
