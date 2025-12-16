import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\8-apply_function_data.csv")
print(df)
print("---------------------")

print(df.head())
print("---------------------")

print(df.tail())
print("---------------------")

print(df.describe())
print("---------------------")

print(df.info())
print("---------------------")

print(df[1:20]) # 1. satırdan 20. satıra kadar
print("---------------------")

print(df.columns) # sütun isimleri
print("---------------------")

def salary_category(salary):
    if salary < 50000:
        return "Low"
    elif 50000 <= salary < 100000:
        return "Medium"
    else:
        return "High"
df['Salary Category'] = df['Salary'].apply(salary_category) # Salary sütununa göre yeni bir sütun ekle 
print(df)
print("---------------------")

# if experience > 10 -> performance_score + 1
def adjust_performance(row):
    if row['Experience'] > 10:
        return row['Performance_Score'] + 1
    else:
        return row['Performance_Score']
df['Adjusted Performance Score'] = df.apply(adjust_performance, axis=1) # Deneyim süresine göre ayarlama
print(df)
print("---------------------")

def adjust_performance(experience):
    if experience > 10:
        return 1
    else:
        return 0

df['Adjustment'] = df['Experience'].apply(adjust_performance) # Deneyim süresine göre ayarlama
print(df)
print("---------------------")

df["New_score"] = df["Performance_Score"] + df["Adjustment"] # Deneyim süresine göre ayarlama
print(df)
print("---------------------")

df["Formatted_Name"] = df["Name"].apply(lambda x: x.replace("_", " ")) # Formatted_Name adında yeni bir sütun oluştur ve alt çizgileri boşluk ile değiştir
print(df)