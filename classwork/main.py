# followers = {
#!     "alex": ["maria", "ivan", "dima"],
#!    "maria": ["alex", "olga"],
#!     "ivan": ["dima"],
#     "dima": ["alex", "maria", "ivan"]
# }

# popular = max(followers, key=lambda user: len(followers[user]))
# print("Найпопулярніший:", popular)

# for user, subs in followers.items():
#     for sub in subs:
#         if user not in followers.get(sub, []):
#             print(f"{user} підписаний на {sub}, але не навзаєм")
            
# sorted_users = sorted(followers, key=lambda u: len(followers[u]), reverse=True)
# print("Топ-3:", sorted_users[:3])

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Meteorite_Landings.csv")

category_counts = df['fall'].value_counts()
print("Розподіл за типом виявлення:")
print(category_counts)

meteorite_types = df['recclass'].value_counts().head(10)
print("\nНайпоширеніші типи метеоритів:")
print(meteorite_types)

plt.figure(figsize=(10, 6))
meteorite_types.plot(kind='bar')
plt.title('Топ-10 найпоширеніших типів метеоритів')
plt.xlabel('Тип метеорита')
plt.ylabel('Кількість')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
