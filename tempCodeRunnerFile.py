import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
sns.set_context('talk')

flights=sns.load_dataset('flights')
print(flights.head())