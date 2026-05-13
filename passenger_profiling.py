import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8,5))
sns.countplot(data=titanic, x='class')

plt.title('Number of Passengers by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')

plt.show()

gender_count = titanic['sex'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Male vs Female Passengers')
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(data=titanic, x='age', bins=20)

plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Amount')

plt.show()

plt.figure(figsize=(8,5))
sns.kdeplot(data=titanic, x='fare', fill=True)

plt.title('Density of Ticket Fare')
plt.xlabel('Fare')
plt.ylabel('Density')

plt.show()

plt.figure(figsize=(8,5))
sns.histplot(data=titanic, x='age', kde=True, bins=20)
plt.title('Age Distribution with KDE Curve')
plt.xlabel('Age')
plt.ylabel('Amount')

plt.show()