import pandas as pd
import numpy as np

df_merge1 = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\7-merge_data1.csv")
df_merge2 = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\7-merge_data2.csv")

# merge - left join
df_merge_left = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="left") # Employee_ID sütununa göre sol birleştirme
print(df_merge_left)
print("---------------------")

# merge - right join
df_merge_right = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="right") # Employee_ID sütununa göre sağ birleştirme
print(df_merge_right)
print("---------------------")

# merge - inner join
df_merge_inner = pd.merge(df_merge1, df_merge2, on="Employee_ID", how="inner") # Employee_ID sütununa göre iç birleştirme
print(df_merge_inner)
print("---------------------")

