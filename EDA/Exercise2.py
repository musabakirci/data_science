import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\VeriBilimiKamp2025\EDA\WineQT.csv")
print(df.head())
print("---------------------")

"""
# pairplot
sns.pairplot(df)
plt.show()
"""

# boxplot grafik
sns.boxplot(x = "quality", y = "alcohol", data = df)
plt.xlabel("Quality")
plt.ylabel("Alcohol")
plt.title("Quality vs Alcohol")
plt.show()

# violin grafik
sns.violinplot(x = "quality", y = "alcohol", data = df)
plt.xlabel("Quality")
plt.ylabel("Alcohol")
plt.title("Quality vs Alcohol")
plt.show()

#scatter plot
sns.scatterplot(x = "pH", y = "alcohol", hue="quality", size = "quality", data = df)
plt.xlabel("pH")
plt.ylabel("Alcohol")
plt.title("Quality vs Alcohol")
plt.show()

sns.scatterplot(x="fixed acidity", y="density", hue="quality", data=df)
plt.xlabel("Fixed Acidity")
plt.ylabel("Alcohol")
plt.title("Quality vs Alcohol")
plt.show()

# Kaggle-GitHub yükleyince gerekecek kodlar!!!!
columns = df.columns
(fig, ax) = plt.subplots(4,4, figsize=(14,13)) # plt.subplots(4,4, ...) → 4x4 = 16 tane boş grafik alanı (subplot) oluşturur. figsize=(14,13) → Çizilecek tüm figürün boyutlarını belirler (14 inç x 13 inç).
ax = ax.flatten()                    # ax.flatten() → ax normalde 4x4 bir matris şeklinde gelir. Bunu tek boyutlu bir listeye çeviriyorsun ki kolayca ax[i] ile erişebilesin.

for i, column in enumerate(columns): # enumerate(columns) → hem index (i) hem de kolon adı (column) verir.
    sns.kdeplot(                     # sns.kdeplot(...) → her kolonun dağılımını (Kernel Density Estimation) çizer.
        data = df,
        x = column,                  # x=column → grafiğin x ekseninde o kolonu kullanır.   
        hue = "quality",             # hue="quality" → quality değişkenini renk değişkeni olarak kullanır.
        ax = ax[i]                   # ax=ax[i] → her plot’u ayrı bir subplot içine çizer.
    )
    ax[i].set_title(f"{column} Distribution") # ax[i].set_title(...) → her grafiğin başlığı kolon adı olur.
    ax[i].set_xlabel(None)                    # ax[i].set_xlabel(...) → her grafiğin x eksenindeki değişkeni olmayacak.

for i in range(i+1, len(ax)):
    ax[i].axis('off')
"""
Eğer kolon sayisi 16 dan küçükse, boş kalan grafik kutulari görünür. Bu kod onlari kapatir (axis('off')).
"""

plt.tight_layout() # sıkışık durumlarda grafikleri daha düzenli hale getirir.
plt.show()
