#unique elements, unordered
from operator import le


myList = [10,20,30,10,20,40,10,20,40]
len(myList) 
print("Liste uzunluğu:", len(myList))

myset = set(myList)
print(myset) # Listedeki benzersiz elemanları gösterir

myset.add(50)
print("Yeni set:", myset)

myset.remove(20)
print("Set 20'yi çıkardıktan sonra:", myset)

myset.discard(30)
print("Set 30'u çıkardıktan sonra:", myset)

myset2 = {40, 50, 60}
print("Yeni set 2:", myset2)

myset = myset.union(myset2)
print("Birleşik set:", myset)

myset = myset.intersection(myset2)
print("Kesişim set:", myset)

countryList = ["tr", "us", "uk", "de", "fr", "jp", "cn", "br"]
len(countryList)
print("Ülke listesi uzunluğu:", len(countryList))

emptyList = []
print("Boş liste:", emptyList)
emptyList.append(3)
emptyList.append(5)
emptyList.append(7)

print(emptyList)

emptySet = {}
print(type(emptySet))  # Bu, bir sözlük oluşturur, set değil

emptySet = set()
print(type(emptySet))  # Bu, bir set oluşturur
len(emptySet)
print("Boş set uzunluğu:", len(emptySet))

emptySet.add(1)
emptySet.add(2)
emptySet.add(3)
emptySet.add(1)
emptySet.add(2)

print(emptySet)

emptyDictionary = dict()
emptyDictionary["key1"] = "value1"
emptyDictionary["key2"] = "value2"
emptyDictionary["key3"] = "value3"
print("Boş sözlük:", emptyDictionary)

# set-dictionary farkı= set benzersiz elemanları tutar, sözlük anahtar-değer çiftlerini tutar
