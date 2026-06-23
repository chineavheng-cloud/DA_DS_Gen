# ============================================================
# Healthcare Costs & Patient Demographics
# Exploratory Data Analysis (EDA)
# ============================================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns
pd.set_option('display.max_columns', None)

# Set visualization style
sns.set(style="whitegrid")

# ============================================================
# Load Dataset
# ============================================================

df = pd.read_csv("insurance.csv")

print("="*60)
print("First 5 Rows")
print("="*60)
print(df.head())

# ============================================================
# Dataset Information
# ============================================================

print("\n")
print("="*60)
print("Dataset Information")
print("="*60)
print(df.info())

# ============================================================
# Shape
# ============================================================

print("\nShape of Dataset:")
print(df.shape)

# ============================================================
# Missing Values
# ============================================================

print("\n")
print("="*60)
print("Missing Values")
print("="*60)
print(df.isnull().sum())

# ============================================================
# Duplicate Rows
# ============================================================

print("\nDuplicate Rows:", df.duplicated().sum())

# ============================================================
# Summary Statistics
# ============================================================

print("\n")
print("="*60)
print("Summary Statistics")
print("="*60)
print(df.describe())

# ============================================================
# Categorical Summary
# ============================================================

print("\n")
print("="*60)
print("Categorical Columns")
print("="*60)

print(df.describe(include='object'))

# ============================================================
# Unique Values
# ============================================================

print("\nUnique Values")

for column in df.columns:
    print(f"{column}: {df[column].nunique()}")

# ============================================================
# Data Types
# ============================================================

print("\nData Types")
print(df.dtypes)

# ============================================================
# Distribution of Age
# ============================================================

plt.figure(figsize=(8,5))
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# ============================================================
# BMI Distribution
# ============================================================

plt.figure(figsize=(8,5))
sns.histplot(df['bmi'], bins=20, kde=True, color='green')
plt.title("BMI Distribution")
plt.show()

# ============================================================
# expenses Distribution
# ============================================================

plt.figure(figsize=(8,5))
sns.histplot(df['expenses'], bins=30, kde=True, color='red')
plt.title("Medical expenses Distribution")
plt.show()

# ============================================================
# Gender Count
# ============================================================

plt.figure(figsize=(6,4))
sns.countplot(x='sex', data=df)
plt.title("Gender Distribution")
plt.show()

# ============================================================
# Smoking Status
# ============================================================

plt.figure(figsize=(6,4))
sns.countplot(x='smoker', data=df)
plt.title("Smoking Status")
plt.show()

# ============================================================
# Region Distribution
# ============================================================

plt.figure(figsize=(8,5))
sns.countplot(x='region', data=df)
plt.title("Region Distribution")
plt.show()

# ============================================================
# Children Distribution
# ============================================================

plt.figure(figsize=(6,4))
sns.countplot(x='children', data=df)
plt.title("Number of Children")
plt.show()

# ============================================================
# Age vs expenses
# ============================================================

plt.figure(figsize=(8,6))
sns.scatterplot(x='age', y='expenses', hue='smoker', data=df)
plt.title("Age vs Medical expenses")
plt.show()

# ============================================================
# BMI vs expenses
# ============================================================

plt.figure(figsize=(8,6))
sns.scatterplot(x='bmi', y='expenses', hue='smoker', data=df)
plt.title("BMI vs Medical expenses")
plt.show()

# ============================================================
# Boxplot expenses by Smoker
# ============================================================

plt.figure(figsize=(6,5))
sns.boxplot(x='smoker', y='expenses', data=df)
plt.title("expenses by Smoking Status")
plt.show()

# ============================================================
# Boxplot expenses by Gender
# ============================================================

plt.figure(figsize=(6,5))
sns.boxplot(x='sex', y='expenses', data=df)
plt.title("expenses by Gender")
plt.show()

# ============================================================
# Boxplot expenses by Region
# ============================================================

plt.figure(figsize=(8,5))
sns.boxplot(x='region', y='expenses', data=df)
plt.title("expenses by Region")
plt.show()

# ============================================================
# Boxplot expenses by Children
# ============================================================

plt.figure(figsize=(8,5))
sns.boxplot(x='children', y='expenses', data=df)
plt.title("expenses by Number of Children")
plt.show()

# ============================================================
# Pairplot
# ============================================================

sns.pairplot(df, hue='smoker')
plt.show()

# ============================================================
# Correlation Matrix
# ============================================================

df_encoded = pd.get_dummies(df, drop_first=True)

plt.figure(figsize=(12,8))
corr = df_encoded.corr()

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Matrix")
plt.show()

# ============================================================
# Average expenses
# ============================================================

print("\nAverage expenses by Gender")
print(df.groupby("sex")["expenses"].mean())

print("\nAverage expenses by Smoker")
print(df.groupby("smoker")["expenses"].mean())

print("\nAverage expenses by Region")
print(df.groupby("region")["expenses"].mean())

print("\nAverage expenses by Children")
print(df.groupby("children")["expenses"].mean())

# ============================================================
# Highest expenses
# ============================================================

print("\nTop 10 Highest Medical expenses")

print(
    df.sort_values(by="expenses", ascending=False)
      .head(10)
)

# ============================================================
# Lowest expenses
# ============================================================

print("\nTop 10 Lowest Medical expenses")

print(
    df.sort_values(by="expenses")
      .head(10)
)

# ============================================================
# Correlation with expenses
# ============================================================

print("\nCorrelation with expenses")

print(
    corr["expenses"]
    .sort_values(ascending=False)
)

# ============================================================
# Outlier Detection
# ============================================================

plt.figure(figsize=(6,5))
sns.boxplot(y=df['expenses'])
plt.title("Outliers in expenses")
plt.show()

plt.figure(figsize=(6,5))
sns.boxplot(y=df['bmi'])
plt.title("Outliers in BMI")
plt.show()

# ============================================================
# Average expenses by Age
# ============================================================

avg_age = df.groupby('age')['expenses'].mean()

plt.figure(figsize=(12,5))
avg_age.plot(marker='o')

plt.title("Average expenses by Age")
plt.xlabel("Age")
plt.ylabel("Average expenses")
plt.grid(True)
plt.show()

# ============================================================
# Pie Chart - Smokers
# ============================================================

plt.figure(figsize=(6,6))

df['smoker'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Smoker Percentage")
plt.ylabel("")
plt.show()

# ============================================================
# Pie Chart - Gender
# ============================================================

plt.figure(figsize=(6,6))

df['sex'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Gender Percentage")
plt.ylabel("")
plt.show()

# ============================================================
# Final Summary
# ============================================================

print("\n")
print("="*60)
print("EDA COMPLETED SUCCESSFULLY")
print("="*60)

print("""
Key Findings:

1. Older patients generally have higher medical expenses.

2. Smokers have significantly higher healthcare costs.

3. Higher BMI is associated with increased medical expenses.

4. Gender has little impact on medical expenses.

5. Regional differences exist but are relatively small.

6. The medical expenses distribution is right-skewed.

7. Smoking status has the strongest correlation with healthcare expenses.
""")