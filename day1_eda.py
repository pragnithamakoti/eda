import pandas as pd
from ydata_profiling import ProfileReport

# Step 1: Load dataset
df = pd.read_csv("housing.csv")

print("✅ Dataset loaded successfully!\n")

# Step 2: Show sample data (clean format)
print("📄 Sample Data:")
print(df.head().to_string())

# Save sample for Word document
df.head().to_csv("sample_output.csv", index=False)

# Step 3: Dataset Info
print("\n📌 Dataset Info:")
df.info()

# Step 4: Statistical Summary
print("\n📊 Statistical Summary:")
print(df.describe())

# Step 5: Missing Values
print("\n❗ Missing Values:")
print(df.isnull().sum())

# Step 6: Generate EDA Report
print("\n⏳ Generating EDA report...")
profile = ProfileReport(df, title="EDA Report", explorative=True)
profile.to_file("eda_report.html")

print("\n🎉 EDA report generated successfully!")
print("📁 Check your folder for 'eda_report.html' and 'sample_output.csv'")