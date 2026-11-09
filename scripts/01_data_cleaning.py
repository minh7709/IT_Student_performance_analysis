"""
BUOC 1 & 2: TIEP NHAN, KHAO SAT & TIEN XU LY LAM SACH DU LIEU
Du an: Phan tich hanh vi & hieu qua hoc tap sinh vien IT/CSE
"""
import os
import sys
import pandas as pd
import numpy as np

# Dam bao terminal Windows ho tro UTF-8
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def clean_data():
    raw_path = os.path.join("archive", "Students_Performance_data_set.csv")
    out_dir = os.path.join("data")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cleaned_students_performance.csv")

    print("[1/5] Loading raw data from:", raw_path)
    df = pd.read_csv(raw_path)
    print(f"Original shape: {df.shape[0]} rows, {df.shape[1]} columns")

    # 1. Rename columns to standardized snake_case
    col_mapping = {
        "University Admission year": "admission_year",
        "Gender": "gender",
        "Age": "age",
        "H.S.C passing year": "hsc_passing_year",
        "Program": "program",
        "Current Semester": "current_semester",
        "Do you have meritorious scholarship ?": "scholarship",
        "Do you use University transportation?": "university_transport",
        "How many hour do you study daily?": "daily_study_hours",
        "How many times do you seat for study in a day?": "study_frequency",
        "What is your preferable learning mode?": "learning_mode",
        "Do you use smart phone?": "use_smartphone",
        "Do you have personal Computer?": "have_pc",
        "How many hour do you spent daily in social media?": "social_media_hours",
        "Status of your English language proficiency": "english_proficiency",
        "Average attendance on class": "attendance_percentage",
        "Did you ever fall in probation?": "probation",
        "Did you ever got suspension?": "suspension",
        "Do you attend in teacher consultancy for any kind of academical problems?": "faculty_consultancy",
        "What are the skills do you have ?": "skills",
        "How many hour do you spent daily on your skill development?": "skill_dev_hours",
        "What is you interested area?": "interest_area",
        "What is your relationship status?": "relationship_status",
        "Are you engaged with any co-curriculum activities?": "extracurricular",
        "With whom you are living with?": "living_with",
        "Do you have any health issues?": "health_issues",
        "What was your previous SGPA?": "previous_sgpa",
        "Do you have any physical disabilities?": "physical_disabilities",
        "What is your current CGPA?": "current_cgpa",
        "How many Credit did you have completed?": "credits_completed",
        "What is your monthly family income?": "monthly_income"
    }
    df = df.rename(columns=col_mapping)

    # 2. Strip whitespace from all string columns
    str_cols = df.select_dtypes(include=['object', 'string']).columns
    for c in str_cols:
        df[c] = df[c].astype(str).str.strip()

    # 3. Fix typo: HSC passing year = 2028 when admission = 2020 -> fix to 2018
    anomalous_hsc = df['hsc_passing_year'] > df['admission_year']
    num_hsc_fixed = anomalous_hsc.sum()
    if num_hsc_fixed > 0:
        df.loc[anomalous_hsc, 'hsc_passing_year'] = 2018
        print(f"[2/5] Fixed {num_hsc_fixed} logical typo in hsc_passing_year (2028 -> 2018).")

    # 4. Standardize attendance_percentage: '94-98' -> 96.0, cast to float
    df['attendance_percentage'] = df['attendance_percentage'].replace({'94-98': '96.0', 'nan': np.nan})
    df['attendance_percentage'] = pd.to_numeric(df['attendance_percentage'], errors='coerce')
    if df['attendance_percentage'].isna().any():
        median_val = df['attendance_percentage'].median()
        df['attendance_percentage'] = df['attendance_percentage'].fillna(median_val)
    print("[3/5] Standardized attendance_percentage to numeric (float64).")

    # 5. Clean categorical values
    health_map = {'No': 'No', 'no': 'No', 'N': 'No', 'Yes': 'Yes'}
    df['health_issues'] = df['health_issues'].map(health_map).fillna('No')

    df['relationship_status'] = df['relationship_status'].replace({'In a relationship': 'Relationship'})

    interest_map = {
        'NETWORKING': 'Networking',
        'Data Schince': 'Data Science',
        'Artificial Intelligence': 'Artificial Intelligence',
        'Machine Learning': 'Machine Learning',
        'Web development': 'Web Development',
        'Software': 'Software Engineering'
    }
    df['interest_area'] = df['interest_area'].replace(interest_map)

    mode_skill = df['skills'].mode()[0]
    df['skills'] = df['skills'].replace({'nan': mode_skill, '': mode_skill}).fillna(mode_skill)

    binary_cols = ['scholarship', 'university_transport', 'use_smartphone', 'have_pc',
                   'probation', 'suspension', 'faculty_consultancy', 'extracurricular',
                   'health_issues', 'physical_disabilities']
    for b in binary_cols:
        df[b] = df[b].str.capitalize()

    # 6. Check duplicate rows
    dups = df.duplicated().sum()
    if dups > 0:
        df = df.drop_duplicates()
        print(f"[4/5] Dropped {dups} duplicate rows.")
    else:
        print("[4/5] No duplicate rows detected.")

    # 7. Save cleaned data
    df.to_csv(out_path, index=False)
    print(f"[5/5] Data cleaning completed! Saved to {out_path} ({df.shape[0]} rows, {df.shape[1]} cols)")
    return df

if __name__ == "__main__":
    clean_data()
