import numpy as np
import pandas as pd

df1 = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\7-concat_data1.csv")
df2 = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\7-concat_data2.csv")

print(df1)
print(df2)

# concat 
df_concat = pd.concat([df1, df2], ignore_index=True) # indexleri 1 den başlat 20 ye kadar sırala birleştir.
print(df_concat)
print("---------------------")

# merge
df_merge1 = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\7-merge_data1.csv")
df_merge2 = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\7-merge_data2.csv")

print(df_merge1)
print(df_merge2)

df_merge_outer = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="outer") # Employee_ID sütununa göre dış birleştirme
print(df_merge_outer)
print("---------------------")
