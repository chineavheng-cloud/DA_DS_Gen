import seaborn as sns
import matplotlib.pyplot as plt
penguins=sns.load_dataset('penguins')
print(penguins.head())

plt.figure(figsize=(10,6))
sns.scatterplot(
    data=penguins,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species',
    style='island',
    size='body_mass_g',
    sizes=(50,250)
)
plt.title("Penguins Species Comparison")
plt.xlabel("Bill length")
plt.ylabel("Bill depth")
plt.show()

sns.pairplot(
    penguins,hue='species'
)
plt.show()

numeric_pen=penguins.select_dtypes(include=['Float64','int64'])
corr_matrix=numeric_pen.corr()
print(corr_matrix)

plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm'
)
plt.title("Penguin feature correlation heatmap")
plt.show()