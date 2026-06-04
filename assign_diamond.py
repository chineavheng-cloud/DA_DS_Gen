import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
diamonds=pd.read_csv('diamonds.csv')
# print(diamonds)
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=diamonds,
    x="carat",
    y="price",
    alpha=0.5
)
plt.title("Diamond price vs Carat weight")
plt.xlabel("Carat")
plt.ylabel("Price $")
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(
    data=diamonds,
    x="cut",
    y="price",
    estimator='mean'
)
plt.title("Average Diamond price by Cut")
plt.xlabel("Cut")
plt.ylabel("Average Price $")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(
    data=diamonds,
    x="color",
    y="price",
    estimator='mean',
    order=['D','E','F','G','H','I','J']
)
plt.title("Average Price by Color grade")
plt.xlabel("Color grade")
plt.ylabel("Average price $")
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(
    data=diamonds,
    x="price",
    bins=50,
    kde=True
)
plt.title("Distribution of Diamond prices")
plt.xlabel("Price $")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8,6))
numeric_diamonds=diamonds.select_dtypes(include=['int64','float64'])
corr=numeric_diamonds.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(
    data=diamonds,
    x="cut",
    y="price"
)
plt.title("Price distribution by cut")
plt.xlabel("Cut")
plt.ylabel("Price (USD)")
plt.show()

selected = diamonds[['price','carat','depth','table']]
sns.pairplot(selected)
plt.show()
summary_table = diamonds.groupby('cut')['price'].agg(
    Average_Price='mean',
    Minimum_Price='min',
    Maximum_Price='max'
)
print(summary_table.round(2))