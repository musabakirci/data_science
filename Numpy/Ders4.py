import numpy as np

#dot product
first_matrix = np.array([[1, 2, 3]])
print(first_matrix)
second_matrix = np.array([[7, 8], [10, 11], [12, 13 ]])
print(second_matrix)
"""
dot product uygulamak için birincinin row sayisi ikincinin column sayisina esit olmalidir.
"""

print("Dot Product", np.dot(first_matrix, second_matrix)) # dot product işlemi yapar