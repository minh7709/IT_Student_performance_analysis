"""
BUOC 3: KY THUAT DAC TRUNG (FEATURE ENGINEERING)
Du an: Phan tich hanh vi & hieu qua hoc tap sinh vien IT/CSE
"""
import os
import sys
import pandas as pd
import numpy as np

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def feature_engineering():
    cleaned_path = os.path.join("data", "cleaned_students_performance.csv")
    out_path = os.path.join("data", "processed_students_performance.csv")

    print("[1/4] Loading cleaned dataset from:", cleaned_path)
    df = pd.read_csv(cleaned_path)

    print("[2/4] Engineering domain features...")
    # 1. Study to Social Media Ratio
    df['study_to_social_ratio'] = df['daily_study_hours'] / (df['social_media_hours'] + 0.1)
    df['study_to_social_ratio'] = df['study_to_social_ratio'].round(3)

    # 2. Gap Year (Between HSC completion and University Admission)
    df['gap_year'] = df['admission_year'] - df['hsc_passing_year']
    df['gap_year'] = df['gap_year'].apply(lambda x: max(0, x))

    # 3. Study Effort Index
    df['study_effort_index'] = df['daily_study_hours'] * df['study_frequency']

    # 4. Academic Support Index (Merit Scholarship + Faculty Consultancy)
    df['academic_support_index'] = (
        (df['scholarship'] == 'Yes').astype(int) +
        (df['faculty_consultancy'] == 'Yes').astype(int)
    )

    # 5. Academic Risk Score (Composite risk indicator)
    df['academic_risk_score'] = (
        (df['probation'] == 'Yes').astype(int) +
        (df['suspension'] == 'Yes').astype(int) +
        (df['attendance_percentage'] < 80.0).astype(int) +
        (df['health_issues'] == 'Yes').astype(int)
    )

    # 6. CGPA - SGPA Trend (Academic Progress)
    df['gpa_progression'] = (df['current_cgpa'] - df['previous_sgpa']).round(2)

    # 7. Pedagogical Target Variable: Student Status
    # Standard Bangladesh university classification rule
    def assign_student_status(row):
        if row['suspension'] == 'Yes' or row['probation'] == 'Yes' or row['current_cgpa'] < 2.50:
            return 'Academic Risk'
        elif row['current_cgpa'] >= 3.50:
            return 'Good Standing'
        else:
            return 'Average Standing'

    df['student_status'] = df.apply(assign_student_status, axis=1)

    print("[3/4] Feature engineering summary:")
    print("New features created:")
    print("  - study_to_social_ratio")
    print("  - gap_year")
    print("  - study_effort_index")
    print("  - academic_support_index")
    print("  - academic_risk_score")
    print("  - gpa_progression")
    print("  - student_status (Target)")
    print("\nTarget Variable Distribution:")
    status_counts = df['student_status'].value_counts()
    for status, count in status_counts.items():
        pct = (count / len(df)) * 100
        print(f"  * {status:16s}: {count:4d} ({pct:.1f}%)")

    # 8. Save processed dataset
    df.to_csv(out_path, index=False)
    print(f"\n[4/4] Processed data saved successfully to: {out_path}")
    print(f"Final dataset dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    feature_engineering()
