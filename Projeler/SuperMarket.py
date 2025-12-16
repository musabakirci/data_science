from calendar import month
import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\VerilerKaggle\SuperMarket\train.csv")
print(df.head())
print("---------------------")

print(df.shape)
print("---------------------")

print(df.describe())
print("---------------------")

print(df.info())
print("---------------------")

print(df.columns)
print("---------------------")

Df = df.drop(["Row ID", "Order ID", "Customer ID", "Product ID"], axis=1)
print(Df)
print("---------------------")

print(Df.head())
print("---------------------")

print(Df.isnull().sum())
print("---------------------")

print(Df[Df["Postal Code"].isnull()])
print("---------------------")

Df["Postal Code"] = Df["Postal Code"].fillna(5402)
print(Df)
print("---------------------")

print(Df.isnull().sum())
print("---------------------") 

print(Df[Df["City"] =="Burlington" ])
print("---------------------")

# month column
Df["Month"] = Df["Order Date"].str[3:5]
print(Df)
print("---------------------")

Df["Month"] = Df["Month"].astype(int)
print(Df)
print("---------------------")

# Month convert to string
d = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

Df["Month"] = Df["Month"].map(d)

print(Df)
print("---------------------")
   
Df["Order Date"] = pd.to_datetime(Df["Order Date"], dayfirst=True)
print(Df)
print("---------------------")

Df["Ship Date"] = pd.to_datetime(Df["Ship Date"], dayfirst=True)
print(Df)
print("---------------------")

Df["Year"] = Df["Order Date"].dt.year
print(Df)
print("---------------------")

print(Df["Year"].value_counts())
print("---------------------")

print(Df["Month"].value_counts())
print("---------------------")

# Hangi ayda satis fazla - DÜZELTME: inplace=True kaldırıldı
months_df = Df.groupby("Month")["Sales"].sum().reset_index()
print(months_df)
print("---------------------")

# Aylara göre toplam satışları büyükten küçüğe sırala
months_df_sorted = months_df.sort_values(by="Sales", ascending=False)
print("Aylara göre satış sıralaması:")
print(months_df_sorted)
print("---------------------")

# Görselleştirme
plt.figure(figsize=(12, 6))
plt.bar(months_df["Month"], months_df["Sales"])
plt.title("Aylara Göre Toplam Satışlar")
plt.xlabel("Aylar")
plt.ylabel("Toplam Satış ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# En çok satış yapılan ay
max_sales_month = months_df_sorted.iloc[0]
print(f"En çok satış yapılan ay: {max_sales_month['Month']} - Toplam Satış: ${max_sales_month['Sales']:,.2f}")
print("---------------------")

# DÜZELTME: df yerine Df kullanılmalı çünkü Year sütunu Df'de
year_df = Df.groupby("Year")["Sales"].sum().reset_index()  # Sadece Sales sütununu topla
print(year_df)
print("---------------------")

# Bar plot için
plt.figure(figsize=(10, 6))
plt.bar(year_df["Year"].astype(str), year_df["Sales"])
plt.title("Yıllara Göre Toplam Satışlar")
plt.xlabel("Yıllar")
plt.ylabel("Toplam Satış ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("---------------------")

# Ek istatistikler
print("Yıllara göre satış istatistikleri:")
print(f"Toplam satış: ${year_df['Sales'].sum():,.2f}")
print(f"Yıllık ortalama satış: ${year_df['Sales'].mean():,.2f}")
print(f"En yüksek yıllık satış: ${year_df['Sales'].max():,.2f} ({year_df.loc[year_df['Sales'].idxmax(), 'Year']} yılı)")
print(f"En düşük yıllık satış: ${year_df['Sales'].min():,.2f} ({year_df.loc[year_df['Sales'].idxmin(), 'Year']} yılı)")