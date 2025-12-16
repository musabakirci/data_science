import numpy as np
import matplotlib.pyplot as plt

age_list = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]
np_age_list = np.array(age_list)
print(np_age_list)

weight_list = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]
np_weight_list = np.array(weight_list)
print(np_weight_list)

plt.plot(np_age_list, np_weight_list, "r")
plt.xlabel("Yaş")
plt.ylabel("Ağırlık")
plt.title("Yaş ve Ağırlık İlişkisi")
plt.show()

numpy_arr1 = np.linspace(0,10,20) # 0 ile 10 arasında 20 eşit parçaya ayır
print(numpy_arr1)

numpy_arr2 = numpy_arr1**3
print(numpy_arr2)

plt.plot(numpy_arr1, numpy_arr2, "b*") # mavi yıldız işareti ile çiz
plt.xlabel("X")
plt.ylabel("Y")
plt.title("X ve Y İlişkisi")
plt.show()