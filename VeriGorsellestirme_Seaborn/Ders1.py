import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\PythonForDataScienceNotebooks-main\PythonForDataScienceNotebooks-main\athlete_events.csv.zip")
print(data)
print("---------------------")

sns.set_style("whitegrid")
sns.scatterplot(x = "Height", y = "Weight", hue="Sex", data = data) # Bu satırda x eksenindeki değişken Height, y eksenindeki değişken Weight, renk değişkeni Sex ve veri seti data olarak belirtiliyor. hue degiskeninde renk belirliyoruz.
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Height vs Weight")
plt.show()

# Belirli kolonlarda işlem yapmak istiyorsak hue değişkenini kullabiliriz.
sns.set_style("whitegrid")
sns.scatterplot(x = "Height", y = "Weight", hue="Medal", data = data) # Bu satırda x eksenindeki değişken Height, y eksenindeki değişken Weight, renk değişkeni Sex ve veri seti data olarak belirtiliyor. hue degiskeninde renk belirliyoruz ve istediğimiz kolonu buraya yazabiliriz
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Height vs Weight")
plt.show()

# Biraz daha ileri gidip style kullanarak daha farklı grafikler olusturabiliriz.
sns.set_style("whitegrid")
sns.scatterplot(x = "Height", y = "Weight", hue="Sex", style="Medal", data = data) # Bu satırda style değişkeni Medal, x eksenindeki değişken Height, y eksenindeki değişken Weight, renk değişkeni Sex ve veri seti dat,a olarak belirtiliyor. hue degiskeninde renk belirliyoruz ve istediğimiz kolonu buraya yazabiliriz
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Height vs Weight")
plt.show()

# Biraz daha ileri gidip style kullanarak daha farklı grafikler olusturabiliriz. size değişkeni de ekleyebiliriz. Bu degiskendeki her bir boyut biriyle iliskili olabilir.
sns.set_style("whitegrid")
sns.scatterplot(x = "Height", y = "Weight", hue="Sex", style="Medal", size="Age", data = data) # Bu satırda style değişkeni Medal, x eksenindeki değişken Height, y eksenindeki değişken Weight, renk değişkeni Sex ve veri seti dat,a olarak belirtiliyor. hue degiskeninde renk belirliyoruz ve istediğimiz kolonu buraya yazabiliriz
plt.xlabel("Height of Athletes")
plt.ylabel("Weight of Athletes")
plt.title("Height vs Weight")
plt.show()