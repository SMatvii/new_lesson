import pandas as pd, numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Ім'я": ['Igor', 'Anna', 'Lenya','Danil','Matvii'],
    "Математика": np.random.randint(1, 13, 5),
    "Фізика": np.random.randint(1, 13, 5),
    "Хімія": np.random.randint(1, 13, 5)
})

df["Середній"] = df[["Математика", "Фізика", "Хімія"]].mean(axis=1)

df["Статус"] = pd.cut(
    df["Середній"],
    bins=[6, 7, 8, 10],
    labels=["Нижче середнього", "Середній", "Відмінник"]
)

df_sorted = df.sort_values("Середній", ascending=False)

print("Таблиця:\n")
print(df_sorted)

df_sorted.plot(x="Ім'я", y="Середній", kind="bar", color="lightgreen", legend=False)
plt.title("Середній бал студентів")
plt.ylabel("Бали")
plt.ylim(0, 12)
plt.show()