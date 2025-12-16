import numpy as np
import pandas as pd

#working with missing data

weather_na_df = pd.read_excel(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\6-weatherna.xlsx")

print(weather_na_df)
print("---------------------")

print(weather_na_df.isna()) # eksik verileri kontrol et
print("---------------------")

print(weather_na_df.isna().sum()) # her sütundaki eksik veri sayısını göster
print("---------------------")

print(weather_na_df.describe()) # istatistiksel özet
print("---------------------")

print(weather_na_df["Paris"]) # Paris sütununu göster
print("---------------------")

print(weather_na_df["Paris"].isna()) # Paris sütunundaki eksik verileri kontrol et
print("---------------------")

print(weather_na_df["Paris"].isna().sum()) # Paris sütunundaki eksik veri sayısını göster
print("---------------------")

print(weather_na_df["Amsterdam"].count()) # Amsterdam sütunundaki geçerli (non-null) veri sayısını göster
print("---------------------")

print(weather_na_df.dropna()) # eksik verileri içeren satırları düşür
print("---------------------")

print(weather_na_df.dropna(axis=1)) # Bir kolonun içinde en az bir eksik veri olan sütunları düşür
print("---------------------")

print(weather_na_df.drop("Paris", axis=1)) # Paris sütununu düşür
print("---------------------")

print(weather_na_df.fillna(44)) # eksik verileri 44 ile doldur
print("---------------------")

print(weather_na_df.mean()) # her sütunun ortalamasını göster
print("---------------------")

print(weather_na_df.median()) # her sütunun medyanını göster
print("---------------------")

print(weather_na_df.fillna(weather_na_df.mean())) # eksik verileri sütun ortalamaları ile doldur
print("---------------------")

print(weather_na_df.max()) # her sütunun maksimum değerini göster
print("---------------------")
