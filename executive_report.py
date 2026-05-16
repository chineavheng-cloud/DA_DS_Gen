import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
sns.set_context('talk')

flights=sns.load_dataset('flights')
print(flights.head())

flights_pivot=flights.pivot(
    index='month',
    columns='year',
    values='passengers'
)
plt.figure(figsize=(12,8))
sns.heatmap(
    flights_pivot,
    cmap=sns.color_palette("Blues",as_cmap=True),
    annot=True,
    fmt='d'
)
plt.title("Passengers per Month (1949-1960)")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()
avg_passengers=flights.groupby('year')['passengers'].mean()

fig,ax=plt.subplots(figsize=(12,6))
ax.plot(
    avg_passengers.index,
    avg_passengers.values,
    marker='o'
)
ax.set_title("Average Flight Passengers Per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Average Passengers")
plt.xticks(rotation=45)
ax.set_ylim(0,500)
ax.annotate(
    "Introduction of the Jets",
    xy=(1960,avg_passengers.loc[1960]),
    xytext=(1954,420),
    arrowprops=dict(arrowstyle='->')
)
plt.tight_layout()
plt.savefig(
    'executive_flight_report.png',
    dpi=300,
    bbox_inches='tight'
)
plt.show()
print("Image saved as executive_flight_report.png")