import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())

plt.figure(figsize=(10,5))
# 1. grafik
plt.subplot(1,2,1)
sns.boxplot(x = "class", y = "age", data = df)
plt.title("Age by Class")
plt.xlabel("Class")
plt.ylabel("Age")
# 2. grafik
plt.subplot(1,2,2)
sns.boxplot(x = "class", y = "fare", data = df)
plt.title("Fare by Class")
plt.xlabel("Class")
plt.ylabel("Fare")

plt.tight_layout() # sıkışık durumlarda grafikleri daha düzenli hale getirir.
plt.show()