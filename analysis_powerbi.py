import pandas as pd

# charger les données
df = pd.read_csv("train.csv", encoding="latin1")

# convertir la date
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")

# créer année et mois
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%B")

# =========================
# 1. KPI PRINCIPAUX
# =========================

total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
average_sales = df["Sales"].mean()

print("=== KPI PRINCIPAUX ===")
print(f"Chiffre d'affaires total : {total_sales:.2f}")
print(f"Nombre total de commandes : {total_orders}")
print(f"Nombre total de clients : {total_customers}")
print(f"Panier moyen / vente moyenne : {average_sales:.2f}")

# =========================
# 2. VENTES PAR CATEGORIE
# =========================

sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\n=== VENTES PAR CATEGORIE ===")
print(sales_by_category)

# =========================
# 3. TOP 10 PRODUITS
# =========================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\n=== TOP 10 PRODUITS ===")
print(top_products)

# =========================
# 4. VENTES PAR ANNEE
# =========================

sales_by_year = df.groupby("Year")["Sales"].sum().sort_values()
print("\n=== VENTES PAR ANNEE ===")
print(sales_by_year)

# =========================
# 5. VENTES PAR MOIS
# =========================

sales_by_month = df.groupby("Month")["Sales"].sum().sort_index()
print("\n=== VENTES PAR MOIS ===")
print(sales_by_month)

# =========================
# 6. TOP 10 ETATS
# =========================

top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
print("\n=== TOP 10 ETATS ===")
print(top_states)

# =========================
# 7. TOP 10 CLIENTS
# =========================

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\n=== TOP 10 CLIENTS ===")
print(top_customers)

# =========================
# 8. EXPORT POUR POWER BI
# =========================

df.to_csv("ecommerce_cleaned.csv", index=False)
sales_by_category.to_csv("sales_by_category.csv")
top_products.to_csv("top_products.csv")
sales_by_year.to_csv("sales_by_year.csv")
sales_by_month.to_csv("sales_by_month.csv")
top_states.to_csv("top_states.csv")
top_customers.to_csv("top_customers.csv")

print("\n=== EXPORT TERMINE ===")
print("Les fichiers CSV pour Power BI ont été créés.")

# Il calcule :
# chiffre d’affaires total
# nombre de commandes
# nombre de clients
# vente moyenne

# Puis il analyse :
# ventes par catégorie
# top produits
# ventes par année
# ventes par mois
# top États
# top clients