myList = [10,"a","b",3,14]
print("Liste:", myList)
print(myList[0])

#tuple
myTuple = (10, "a", "b", 3, 14)
print("Tuple:", myTuple)
print(type(myTuple))
print(myTuple[0])
myTuple[0] = 20  # Bu satır hata verecektir çünkü tuple'lar değiştirilemez
print(myTuple.index("a"))  # "a" elemanının indeksi
print(myTuple.count(10))  # 10 elemanının sayısı