import os
import pandas as pd
import numpy as np

file_path = os.path.join("archive", "Students_Performance_data_set.csv")
df = pd.read_csv(file_path)

print("--- Attendance unique values (all non-integer / string values) ---")
att = df["Average attendance on class"]
for val in att.unique():
    try:
        float(val)
    except ValueError:
        print(f"Non-numeric attendance value: '{val}' (count: {(att == val).sum()})")

print("\n--- Rows with attendance <= 50 or other strange values ---")
numeric_att = pd.to_numeric(att, errors='coerce')
print("Null count when coerced:", numeric_att.isna().sum())
print("Non-numeric rows:")
print(df[numeric_att.isna()][["Current Semester", "Average attendance on class", "What is your current CGPA?"]])

print("\n--- HSC passing year anomalies ---")
print("HSC passing year > 2024:")
print(df[df["H.S.C passing year"] > 2024][["University Admission year", "H.S.C passing year", "Age"]])

print("HSC passing year < 2010:")
print(df[df["H.S.C passing year"] < 2010][["University Admission year", "H.S.C passing year", "Age"]])

print("\n--- University Admission Year vs HSC passing year ---")
df['diff'] = df["University Admission year"] - df["H.S.C passing year"]
print("Negative diff (Admission before HSC?!):", (df['diff'] < 0).sum())
print(df[df['diff'] < 0][["University Admission year", "H.S.C passing year", "Age", "diff"]])

print("\n--- Academic probation & suspension vs CGPA ---")
print(df.groupby(["Did you ever fall in probation?", "Did you ever got suspension?"])["What is your current CGPA?"].agg(['count', 'mean', 'min', 'max']))

print("\n--- CGPA distribution percentiles ---")
print(df["What is your current CGPA?"].describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9]))
