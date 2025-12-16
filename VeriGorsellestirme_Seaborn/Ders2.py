import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\athlete_events.csv.zip")
print(data)
print("---------------------")

# Çizgi grafiği
sns.set_style("whitegrid")
sns.lineplot(x = "Height", y = "Weight", hue = "Sex", data = data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Height vs Weight")
plt.show()
"""
Burada y eksenindeki değişken Weight, x eksenindeki değişken Height, renk değişkeni Sex ve veri seti data olarak belirtiliyor. hue degiskeninde renk belirliyoruz. 
"""

# Kum grafik
sns.set_style("whitegrid")
sns.displot(x = "Height", hue = "Sex", data = data)
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.show()
"""
Burada x eksenindeki değişken Height, renk değişkeni Sex ve veri seti data olarak belirtiliyor. hue degiskeninde renk belirliyoruz. Sıklık grafiklerinde renk belirliyoruz.
"""

# Kum grafik
sns.set_style("whitegrid")
sns.displot(x = "Height", hue = "Sex", data = data, kind = "kde") # kind degerini kde olarak değiştirerek kum grafik olusturabiliriz. kde = kum denklemini kullanarak kum grafik olusturur.
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.show()
"""
Burada x eksenindeki değişken Height, renk değişkeni Sex ve veri seti data olarak belirtiliyor. hue degiskeninde renk belirliyoruz. kind degiskeninde kum grafik olusturmak istiyorsak kind degerini kde olarak değiştirerek kum grafik olusturabiliriz.
"""

#barplot
sns.set_style("whitegrid")
sns.barplot(x = "Medal", y = "Height", hue = "Sex", data = data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Medals by Height")
plt.show()

#Catplot
sns.catplot(x = "Medal", y = "Height", hue = "Sex", col="Season", data = data)
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Medals by Height")
plt.show()


#Heatmap
sns.set_style("whitegrid")
sns.heatmap(data.corr(numeric_only=True), annot = True) # numeric_only=True sayesinde sadece numeric degerlerin korelasyonunu hesaplayacak ve korelasyon degerlerini gostericek(annot = True)
plt.show()