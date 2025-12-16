import array
import numpy as np

new_array = np.random.randint(1,100,20)
print(new_array)

print(new_array > 25) # 25'ten büyük olan elemanların boolean dizisi

print(new_array[new_array > 25]) # 25'ten büyük olan elemanları verir


# transpose & reshape
matrix_array = np.array([[10,20],[30,40],[50,60]])
print(matrix_array)
print("*****************************")
print(matrix_array.shape) # matrisin boyutlarını verir
print("*****************************")
print(matrix_array.transpose()) # transpose işlemi
print("*****************************")
"""
transpose = Bu işlem matrisin satir ve sütunlarini yer degistirir.
"""
print(matrix_array.reshape(2,3)) # matrisi 2 satır 3 sütun yapar
print("*****************************")
print(matrix_array.reshape(3,2)) # matrisi 3 satır 2 sütun yapar
"""
reshape = Bu işlem matrisin boyutlarini değiştirir.
"""

# z-score
data = np.array([10, 20, 30, 40, 50, 78, 18, 83, 98])
print("data:", data)
print("*****************************")
mean = np.mean(data)
print("mean:", mean)
print("*****************************")
std = np.std(data)
print("std:", std)
print("*****************************")
z_scores = (data - mean) / std
print("z_scores:", z_scores)
print("*****************************")
print("Outliers:", data[z_scores > 1]) # z-score değeri 1'den büyük olan elemanları verir

"""
z-score = Bu işlem verinin standart sapmaya göre normalize edilmesini sağlar.
"""

# Math equations
"""
2x + 3y = 8 and
4x - y = 2
"""
#coefficients
A = np.array([[2, 3], [4, -1]]) # x ve y'nin katsayıları

# constants
B = np.array([8, 2]) # denklemin sabit terimleri

#Çözüm
solution = np.linalg.solve(A, B)
print("Çözüm:", solution)