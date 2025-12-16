myList = [1, 2, 3, 4, 5]
print("Liste:", myList)

myList[3] = 10
print("Güncellenmiş Liste:", myList)

myList.append(6)
print("Listeye eklenen elemanla birlikte güncellenmiş Liste:", myList)

myList.count(2)
print("Liste içinde 2 sayısı:", myList.count(2), "kez bulunuyor.")

myList.remove(10)
print("10 sayısı listeden çıkarıldı. Güncellenmiş Liste:", myList)

myList.insert(2, 20)
print("20 sayısı 2. indekse eklendi. Güncellenmiş Liste:", myList)

myList.pop(1)
print("1. indeksteki eleman çıkarıldı. Güncellenmiş Liste:", myList)