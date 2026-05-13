import panda as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='darkgrid')
tips=sns.load_dataset('tips')#random data
print(tips.head())

plt.figure(figsize=(8,5))
sns.scatterplot(
    data=tips,
    x='total_bill',y='tip'
)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

plt.figure(figsize=(10,5))
sns.lineplot(
    data=tips.head(20),
    x=tips.head(20).index,
    y='total_bill',
    marker='o'
)
plt.title('Timeline of Total Bills')
plt.xlabel('Order Number')
plt.ylabel('Total Bill')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill'
)
plt.title('Total Bill by day')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()


plt.figure(figsize=(8,5))
sns.violinplot(
    data=tips,
    x='time',
    y='tip'
)
plt.title('Tip Distribution by Time')
plt.xlabel('Meal Time')
plt.ylabel('Tip')
plt.show()


plt.figure(figsize=(8,5))
sns.barplot(
    data=tips,
    x='size',
    y='tip'
)
plt.title('Average Tip by Party Size')
plt.xlabel('Party size')
plt.ylabel('Average Tip')
plt.show()