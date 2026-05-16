import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
mpg=sns.load_dataset('mpg')
print(mpg.head())
sns.relplot(
    data=mpg,
    x='weight',
    y='mpg',
    col='origin',
    hue='origin',
    height=5,
    aspect=1
)
plt.show()

sns.jointplot(
    data=mpg,
    x='horsepower',
    y='mpg',
    kind='scatter',
    height=7
)
plt.show()