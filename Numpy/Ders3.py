import numpy as np

# row * column
numpy_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(numpy_matrix)

print(numpy_matrix.sum())
print(numpy_matrix.mean())
print(numpy_matrix.max())
print(numpy_matrix.min())

#matrix arithmetic
first_array = np.array([[1, 2, 3], [4, 5, 6]])
second_array = np.array([[7, 8, 9], [10, 11, 12]])

print("------------------------")

print("Toplam" ,first_array + second_array)
print("------------------------")
print("Fark" ,first_array - second_array)
print("------------------------")
print("Çarpım" ,first_array * second_array)
print("------------------------")
print("Bölüm" ,first_array / second_array)
print("------------------------")