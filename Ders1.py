import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")
print("Veri setinin tamamı:")
print(df)
print("---------------------")

# Eksik değerleri kontrol etme (True/False formatında)
print("Eksik değer kontrolü (True = eksik):")
print(df.isnull())
print("---------------------")

# Her sütundaki eksik değerlerin toplamı
print("Sütunlara göre eksik değer sayıları:")
print(df.isnull().sum())
print("---------------------")

# 'deck' sütunundaki benzersiz değerler
print("Deck sütunundaki benzersiz değerler:")
print(df["deck"].unique())
print("Unique: ---------------------")

# Veri setinin boyutları (satır ve sütun sayısı)
print("Veri seti boyutu (satır, sütun):")
print(df.shape)
print("Shape: ---------------------")

# Veri seti hakkında genel bilgiler
print("Veri seti bilgileri:")
print(df.info())
print("İnfo: ---------------------")

# Sayısal sütunların istatistiksel özeti
print("Sayısal sütunların istatistiksel özeti:")
print(df.describe())
print("Describe: ---------------------")

# İlk 5 satırı göster
print("İlk 5 kayıt:")
print(df.head())
print("---------------------")

# Eksik değer içeren tüm satırları sil
print("Eksik değerler silindikten sonra:")
print(df.dropna())
print("---------------------")

# Eksik değer doldurma (imputation) işlemleri
# Ortalama ile doldurma (mean imputation)

# Yaş dağılımını görselleştirme
sns.histplot(data=df["age"], kde=True)
plt.xlabel("Yaş")
plt.ylabel("Sayı")
plt.title("Yaş Dağılımı")
plt.show()

# Eksik yaş değerlerini ortalama ile doldurma
df["Age_mean"] = df["age"].fillna(df["age"].mean())
print("Orijinal yaş ve ortalama ile doldurulmuş yaş değerleri:")
# DÜZELTME: Birden fazla sütunu seçmek için çift köşeli parantez kullanılmalı
print(df[["age", "Age_mean"]]) 
print("---------------------")

# Yaş değişkeni için kutu grafiği (boxplot)
sns.boxplot(data=df, y="age")
plt.title("Yaş Değişkeni Kutu Grafiği")
plt.show()

# Medyan ile doldurma işlemi (önce bu sütunu oluşturalım)
df["age_median"] = df["age"].fillna(df["age"].median())

print("Üç farklı yaş sütunu (orijinal, ortalama, medyan):")
# DÜZELTME: Birden fazla sütunu seçmek için çift köşeli parantez kullanılmalı
print(df[["age_median", "Age_mean", "age"]])  
print("---------------------")

# mode imputation -> categorical values
print(df.isnull().sum()) # Eksik degerleri gosterir
print("---------------------")

print(df[df["embarked"].isnull()]) # Embarked sütununda eksik degerleri gosterir
print("---------------------")

print(df["embarked"].unique()) # Embarked sütununda benzersiz degerleri gosterir
print("---------------------")

mode_value = df[df["embarked"].notna()]["embarked"].mode() # Embarked sütununda eksik degerleri gosterir, sonra mode degerini gosterir
print(mode_value) # Mode degerini gosterir
print("---------------------")

df["embarked_mode"] = df["embarked"].fillna(mode_value[0]) # Embarked sütununda eksik degerleri gosterir, sonra mode degerini gosterir
print(df[["embarked", "embarked_mode"]])
print("---------------------")

print(df["embarked"].isnull().sum())
print("---------------------")

print(df["embarked_mode"].isnull().sum())
print("---------------------")