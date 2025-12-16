import numpy as np

#array artimatic
mylist1 = [2,3,4]
mylist2 = [5,6,7]
c = mylist1 + mylist2
print(c) #listelerde toplama islemi concatination yapar ve yan yana dizilir

my_numpy_array1 = np.array(mylist1)
my_numpy_array2 = np.array(mylist2)
my_numpy_array3 = my_numpy_array1 + my_numpy_array2
print(my_numpy_array3) #numpy arraylerde toplama islemi element wise toplama yapar ve değerleri toplar

np_carpim = my_numpy_array1 * my_numpy_array2
print(np_carpim) #numpy arraylerde carpma islemi element wise carpma yapar ve değerleri çarpar

np_bolme = my_numpy_array2 / my_numpy_array1
print(np_bolme) #numpy arraylerde bolme islemi element wise bolme yapar ve değerleri böler

np_cikarma = my_numpy_array2 - my_numpy_array1
print(np_cikarma) #numpy arraylerde cikarma islemi element wise cikarma yapar ve değerleri çıkarır

print("Üs Alma:", my_numpy_array1 ** 2) #numpy arraylerde üs alma islemi element wise üs alma yapar ve değerleri üssünü alır
print("Üs Alma:", my_numpy_array2 ** 2) #numpy arraylerde üs alma islemi element wise üs alma yapar ve değerleri üssünü alır

other_array = np.array([8, 9, 10])
print("Diğer Dizi:", other_array)

print("Diğer Dizi Üst:", other_array.max()) #dizinin en büyük elemanını verir
print("Diğer Dizi Alt:", other_array.min()) #dizinin en küçük elemanını verir
print("Diğer Dizi Ort:", other_array.mean()) #dizinin ortalamasını verir
print("Diğer Dizi Toplam:", other_array.sum()) #dizinin elemanlarının toplamını verir