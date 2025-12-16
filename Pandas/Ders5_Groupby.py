import numpy as np
import pandas as pd

#groupby

df = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\6-employee.csv")
print(df)
print("---------------------")

print(df.describe()) # istatistiksel özet
print("---------------------")

print(df.count()) # her sütundaki geçerli (non-null) veri sayısını göster
print("---------------------")

print(df[df["Experience"]>6].count()) # 6 yıldan fazla deneyimi olan çalışanların sayısını göster
print("---------------------")

df_grouped = df.groupby("Department") # department'a göre grupla
print(df_grouped.count()) # her departmandaki çalışan sayısını göster
print("---------------------")

print(df_grouped.describe()) # her departmandaki çalışanların istatistiksel özetini göster
print("---------------------")

print(df_grouped["Salary"].mean()) # her departmandaki çalışanların ortalama maaşını göster
print("---------------------")

df_grouped2 = df.groupby("City") # şehir'e göre grupla
print(df_grouped2.count()) # her şehirdeki çalışan sayısını göster
print("---------------------")

print(df_grouped2.describe()) # her şehirdeki çalışanların istatistiksel özetini göster
print("---------------------")

print(df_grouped2["Salary"].mean()) # her şehirdeki çalışanların ortalama maaşını göster
print("---------------------")

