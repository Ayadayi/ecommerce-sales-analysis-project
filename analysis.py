import pandas as pd

# charger les données
df = pd.read_csv("train.csv")

# aperçu
print("=== HEAD ===")
print(df.head())

print("\n=== COLUMNS ===")
print(df.columns)

print("\n=== INFO ===")
df.info()

# nettoyer la date
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")

# créer année et mois
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

print("\n=== DESCRIBE ===")
print(df.describe(include="all"))

# - head() : affiche les 5 premières lignes
# - columns : affiche les noms des colonnes
# - info() : affiche le nombre de lignes, colonnes, types et valeurs manquantes
# - describe() : affiche les statistiques principales (moyenne, min, max, etc.)