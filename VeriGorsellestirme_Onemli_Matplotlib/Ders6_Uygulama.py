import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\athlete_events.csv.zip")
print(data)
print("---------------------")

print(data.columns) # sütun isimleri
print("---------------------")

print(data.info())
print("---------------------")

print(data.head())
print("---------------------")

print(data.tail())
print("---------------------")

plt.scatter("Height", "Weight", data=data)
plt.ylabel("Weight")
plt.xlabel("Height")
plt.title("Weight vs Height")
plt.show()