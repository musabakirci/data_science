import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\VeriBilimiKamp2025\EDA\WineQT.csv")
print(df.head())
print("---------------------")

print(df.describe())
print("---------------------")

print(df.info())
print("---------------------")

print(df["quality"].unique())
print("---------------------")

print(df["pH"].unique())
print("---------------------")

print(df.isnull())
print("---------------------")

print(df[df.duplicated()]) # tekrar eden verileri gosterir
print("*---------------------")

print(df.corr())
print("---------------------")

#heatmap
"""
korelasyon degerlerinin heatmap olarak gosterilmesi
"""
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot = True)
plt.xlabel("Features")
plt.ylabel("Features")
plt.title("Correlation Heatmap")
plt.show()


print(df.groupby("quality").mean()) # quality degerlerine gore ortalama degerleri verir
print("---------------------*")

print(df["quality"].value_counts()) # quality degerlerinin sayısını verir
print("---------------------")

print(df["quality"].value_counts().plot(kind="bar")) # grafik olusturur
plt.xlabel("Quality")
plt.ylabel("Count")
plt.title("Quality Distribution")
plt.show()

# pH dagiliminin histogram grafigi
sns.histplot(df["pH"], kde = True) # kde, kum degerlerini gosterir.
plt.xlabel("pH")
plt.ylabel("Count")
plt.title("pH Distribution")
plt.show()

# alcohol dagiliminin histogram grafigi
sns.histplot(df["alcohol"], kde = True, color = "red") # kde, kum degerlerini gosterir.
plt.xlabel("pH")
plt.ylabel("Count")
plt.title("pH Distribution")
plt.show()