import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

numpy_arr1 = np.linspace(0,10,20) # 0 ile 10 arasında 20 eşit parçaya ayır
print(numpy_arr1)

numpy_arr2 = numpy_arr1**3
print(numpy_arr2)

# yan yana grafikleri çizmek için aşagidaki adimlar uygulanir
plt.subplot(1,2,1) # Burada 1 row 2 kolon 1. grafiği çizer
plt.plot(numpy_arr1, numpy_arr2, "r*-")
plt.subplot(1,2,2) # Burada 1 row 2 kolon 2. grafiği çizer
plt.plot(numpy_arr2, numpy_arr1, "g--")
plt.show()

# figure olusturma
my_figure = plt.figure()
figure_axes = my_figure.add_axes([0.1,0.1,0.8,0.8]) # Sırasıyla soldan alttan 0.1, saga uste 0.8, genisligi 0.8, yuksekligi 0.8 olacak şekilde ayarlar
figure_axes.plot(numpy_arr1, numpy_arr2, "r")
figure_axes.set_xlabel("X Axis")
figure_axes.set_ylabel("Y Axis")
figure_axes.set_title("X ve Y İlişkisi")
plt.show()

# figure olusturma
new_fig = plt.figure(dpi=100) # DPI degeri 100 olacak sekilde ayarlar, DPI degeri grafiklerin kalitesini belirler
new_axes = new_fig.add_axes([0.1,0.1,0.9, 0.9]) # Sırasıyla soldan alttan 0.1, saga uste 0.9, genisligi 0.9, yuksekligi 0.9 olacak sekilde ayarlar
new_axes.plot(numpy_arr1, numpy_arr1 **2, label ="numpy aray **2") # label degeri grafiklerin uzerindeki etiketlerini belirler
new_axes.plot(numpy_arr1, numpy_arr1 **3, label ="numpy aray **3")
new_axes.legend(loc = "upper left") # grafiklerin uzerindeki etiketleri belirler
plt.show()