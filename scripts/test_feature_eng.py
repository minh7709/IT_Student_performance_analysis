import os
import sys
import pandas as pd
import numpy as np

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv(os.path.join("data", "cleaned_students_performance.csv"))

# Test thresholds for student_status
def assign_status(row):
    # If student ever got suspension or probation, or CGPA < 2.50, or attendance < 70
    if row['suspension'] == 'Yes' or row['probation'] == 'Yes' or row['current_cgpa'] < 2.50:
        return 'Academic Risk'
    elif row['current_cgpa'] >= 3.50:
        return 'Good Standing'
    else:
        return 'Average Standing'

df['student_status'] = df.apply(assign_status, axis=1)
print("Student Status Distribution:")
print(df['student_status'].value_counts())
print("\nPercentage:")
print(df['student_status'].value_counts(normalize=True) * 100)

print("\nMean CGPA by Status:")
print(df.groupby('student_status')['current_cgpa'].agg(['count', 'mean', 'std', 'min', 'max']))

print("\nMean Attendance by Status:")
print(df.groupby('student_status')['attendance_percentage'].agg(['mean', 'median']))

print("\nMean Daily Study Hours by Status:")
print(df.groupby('student_status')['daily_study_hours'].agg(['mean', 'median']))

print("\nMean Social Media Hours by Status:")
print(df.groupby('student_status')['social_media_hours'].agg(['mean', 'median']))
