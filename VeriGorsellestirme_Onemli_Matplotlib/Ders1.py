import numpy as np
import matplotlib.pyplot as plt

age_list = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]
weight_list = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]
plt.plot(age_list, weight_list, "r") # Kırmızı renk ile çiz
plt.xlabel("Yaş")
plt.ylabel("Ağırlık")
plt.title("Yaş ve Ağırlık İlişkisi")
plt.savefig("yas_agirlik_iliskisi.png") # Grafik dosyasını kaydet. Oluşan dosya "yas_agirlik_iliskisi.png" olarak adlandırılacak.
plt.show()
