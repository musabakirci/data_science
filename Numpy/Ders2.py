import numpy as np

# arange & indexing

print(np.arange(0,10)) # 0'dan 10'a kadar olan sayıları içeren bir dizi oluşturur
print(np.arange(0,11,2)) # 0'dan 10'a kadar olan sayıları içeren bir dizi oluşturur, 2'şer artarak

np_array = np.arange(0,11)
print(np_array) # 0'dan 10'a kadar olan sayıları içeren bir dizi oluşturur

print(np_array[0]) # dizinin ilk elemanını verir
print(np_array[-1]) # dizinin son elemanını verir
print(np_array[::-1]) # dizinin tersini verir

#random

print(np.random.randn(5)) # 5 rastgele sayı üretir
print(np.random.randn(4,4)) # 4x4 rastgele sayı matrisi üretir
print(np.random.randint(1,100,5)) # 1 ile 100 arasında rastgele 5 tam sayı üretir