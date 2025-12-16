my_boolean = True
print(type(my_boolean))
print(5 < 3)  # False

maas = input("Maaşınızı giriniz: ")
print("Maaşınız:", maas)

if int(maas) < 5000 and my_boolean:
    print("Maaşınız 5000 TL'den düşük.")
else:
    print("Maaşınız 5000 TL veya daha yüksek.")
