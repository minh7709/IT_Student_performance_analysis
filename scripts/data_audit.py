import os
import json
import pandas as pd
import numpy as np

# Load dataset
file_path = os.path.join("archive", "Students_Performance_data_set.csv")
df = pd.read_csv(file_path)

print("="*60)
print(f"Dataset Shape: {df.shape}")
print("="*60)

print("\n--- Columns List (31 columns) ---")
for idx, col in enumerate(df.columns, 1):
    print(f"{idx:2d}. {col} (dtype: {df[col].dtype}, non-null: {df[col].count()})")

print("\n--- Missing Values ---")
null_counts = df.isnull().sum()
print(null_counts[null_counts > 0] if (null_counts > 0).any() else "No missing values found!")

print("\n--- Check Duplicates ---")
num_dups = df.duplicated().sum()
print(f"Duplicate rows: {num_dups}")

print("\n--- Numerical Columns Summary ---")
num_cols = df.select_dtypes(include=[np.number]).columns
print(df[num_cols].describe().T[['count', 'mean', 'std', 'min', '50%', 'max']])

print("\n--- Categorical Columns Summary ---")
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    val_counts = df[col].value_counts()
    print(f"\n[{col}] ({len(val_counts)} unique values):")
    print(val_counts.head(5).to_dict())

# Specific checks requested by workflow:
print("\n--- SGPA & CGPA Analysis ---")
sgpa_col = "What was your previous SGPA?"
cgpa_col = "What is your current CGPA?"
if sgpa_col in df.columns:
    print(f"{sgpa_col}: min={df[sgpa_col].min()}, max={df[sgpa_col].max()}, top 5 common values:")
    print(df[sgpa_col].value_counts().head(5))
if cgpa_col in df.columns:
    print(f"{cgpa_col}: min={df[cgpa_col].min()}, max={df[cgpa_col].max()}, top 5 common values:")
    print(df[cgpa_col].value_counts().head(5))

print("\n--- Probation & Suspension Counts ---")
if "Did you ever fall in probation?" in df.columns:
    print("Probation:", df["Did you ever fall in probation?"].value_counts().to_dict())
if "Did you ever got suspension?" in df.columns:
    print("Suspension:", df["Did you ever got suspension?"].value_counts().to_dict())

# Check if there is any target column or mention of student status
status_cols = [c for c in df.columns if "status" in c.lower()]
print(f"\nColumns containing 'status': {status_cols}")

