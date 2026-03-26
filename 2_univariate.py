import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load dataset (FIXED)
df = pd.read_csv("housing.csv", delim_whitespace=True)

# Step 2: Check dataset
print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# Step 3: Setup
sns.set(style="whitegrid")

# Save path (Downloads folder)
save_path = "C:\\Users\\Pragnitha\\Downloads"
print("\nSaving images in:", save_path)

# Step 4: Select numeric columns
numeric_cols = df.select_dtypes(include=['int64','float64']).columns[:2]

print("\nUsing columns for plotting:", numeric_cols)

# Step 5: Histogram
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f"Histogram of {col}")
    plt.savefig(os.path.join(save_path, f"{col}_hist.png"))
    plt.close()

# Step 6: Boxplot
for col in numeric_cols:
    plt.figure()
    sns.boxplot(x=df[col].dropna())
    plt.title(f"Boxplot of {col}")
    plt.savefig(os.path.join(save_path, f"{col}_box.png"))
    plt.close()

print("\nGraphs generated successfully ✅")