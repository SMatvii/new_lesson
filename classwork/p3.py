import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Meteorite_Landings.csv")
df['mass'] = pd.to_numeric(df['mass'], errors='coerce')

mean_mass = df['mass'].mean()
print("Середня маса метеоритів:", mean_mass)


df.rename(columns={
    'name': 'Meteorite Name',
    'mass': 'Mass',
    'year': 'Year'
}, inplace=True)

print("\nПерші 5 рядків:\n", df.head())


df['Mass'].fillna(mean_mass, inplace=True)
df['recclass'].fillna('Unknown', inplace=True)


df_clean = df.dropna(subset=['reclat', 'reclong'])
print("\nТаблиця без пропусків у координатах:\n", df_clean.head())


df['IsLarge'] = df['Mass'] > 1000
print("\nПриклад нового стовпця:\n", df[['Meteorite Name', 'Mass', 'IsLarge']].head())

us_meteorites = df[df['fall'] == 'Fell']
print("\nМетеорити, які впали:\n", us_meteorites.head())


new_meteorite = pd.DataFrame({
    'Meteorite Name': ['MyMeteor'],
    'Mass': [500],
    'Year': [2025],
    'reclat': [50.0],
    'reclong': [30.0],
    'fall': ['Found'],
    'recclass': ['L5'],
    'IsLarge': [False]
})

df = pd.concat([df, new_meteorite], ignore_index=True)
print("\nОстанні рядки з новим метеоритом:\n", df.tail())