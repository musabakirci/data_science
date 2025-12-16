import numpy as np
import pandas as pd

weather_df = pd.read_excel(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\6-weather.xlsx") # Hava durumu verilerini oku
print(weather_df)
print("---------------------")
print(weather_df.head()) # İlk 5 satırı getirir.
print("---------------------")
print(weather_df.tail()) # Son 5 satırı getirir.
print("---------------------")
print(weather_df.info()) # Veri çerçevesi hakkında bilgi verir.
print("---------------------")
print(weather_df.describe()) # Sayısal sütunlar için istatistiksel özet sağlar.
print("---------------------")
print(weather_df.count()) # Her sütundaki geçerli (non-null) değerlerin sayısını getirir.
print("---------------------")
print(weather_df.isna()) # Her sütundaki eksik (null) değerlerin durumunu gösterir.
