a = 10
b = 20
c = a + b
print("Toplam:", c)
str(c)
print("Toplamın string hali:", str(c))
print(type(c))

k = "145"
print("K değişkeninin tipi:", type(k))

float(k)
print("K değişkeninin float hali:", float(k))

namelist = ["Alice", "Bob", "Charlie", "David", "l", "s"]
print("Name list:", namelist)

#nestedlist
nestedlist = [["Alice", 25, 12], ["Bob", 30, 15], ["Charlie", 35, 20]]
print("Nested list:", nestedlist)

smallist = nestedlist[2]
print("Small list:", smallist)

nestedlist[2][1]
print("Nested list içindeki 2. listenin 1. elemanı:", nestedlist[2][1])