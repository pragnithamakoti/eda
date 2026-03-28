import pandas as pd
from scipy import stats

# Step 1: Load dataset (FIXED)
df = pd.read_csv("housing.csv", sep='\s+', header=None)

# Step 2: Add column names
df.columns = [f"Feature_{i}" for i in range(df.shape[1])]

# Step 3: Show dataset
print("First 5 rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

# Step 4: Convert to numeric (safety)
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Step 5: Drop missing values
df = df.dropna()

# Step 6: Select one column
col = df.select_dtypes(include=['int64','float64']).columns[0]

print("\nUsing column:", col)

# -----------------------------
# 1. Shapiro Test (Normality)
# -----------------------------
stat, p = stats.shapiro(df[col])

print("\nShapiro Test:")
print("Statistic:", stat)
print("p-value:", p)

if p > 0.05:
    print("Data is normally distributed ✅")
else:
    print("Data is NOT normally distributed ❌")

# -----------------------------
# 2. T-Test (Split into 2 groups)
# -----------------------------
data1 = df[col][:len(df)//2]
data2 = df[col][len(df)//2:]

t_stat, t_p = stats.ttest_ind(data1, data2)

print("\nT-Test:")
print("t-statistic:", t_stat)
print("p-value:", t_p)

if t_p > 0.05:
    print("No significant difference")
else:
    print("Significant difference exists")

print("\nStatistical testing completed ✅")