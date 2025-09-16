import numpy as np
import pandas as pd

students = ['Igor', 'Anna', 'Lenya','Danil','Matvii']

df = pd.DataFrame({
    "Ім`я": students,
    "Математика": np.random.randint(30, 101, size=5),
    "Фізика": np.random.randint(30, 101, size=5),
    "Хімія": np.random.randint(30, 101, size=5), 
})

df["Середній бал"] = df[["Математика","Фізика","Хімія"]].mean(axis=1)

def get_status(avg):
    if avg >= 75:
        return "Відмінник"
    elif avg >= 50:
        return "Середній"
    else:
        return "Нижче середнього"
    
df["Статус"] = df["Середній бал"].apply(get_status)

df_sorted = df.sort_values(by="Середній бал", ascending=False)

print("Таблиця:\n")
print(df_sorted)
