import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
hours = [1, 2, 3, 4, 5, 6]
med_A_pain = [8, 6, 5, 3, 2, 2]
med_B_pain = [8, 7, 6, 5, 4, 3]

fig, ax = plt.subplots()
ax.plot(
    hours,
    med_A_pain,
    color='blue',
    marker='o',
    label='Medication A'
)
ax.plot(
    hours,
    med_B_pain,
    color='red',
    marker='s',
    label='Medication B'
)
ax.set_title("Pain Level Over Time: Med A vs. Med B")
ax.set_xlabel("Hours Post-Dose")
ax.set_ylabel("Reported Pain Level (0-10)")
ax.legend()
plt.show()