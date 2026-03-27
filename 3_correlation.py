import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load dataset (same fix as Day 2)
df = pd.read_csv("housing.csv", delim_whitespace=True)

# Convert to numeric (important)
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Select numeric data only
df_numeric = df.select_dtypes(include=['int64','float64'])

# Correlation matrix
corr = df_numeric.corr()

# Save path
save_path = "C:\\Users\\Pragnitha\\Downloads"

# Plot heatmap
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.savefig(os.path.join(save_path, "correlation_heatmap.png"))
plt.close()

print("Heatmap generated successfully ✅")