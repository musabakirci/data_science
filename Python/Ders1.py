barcode = "Abdcgehros"

# barkodun uzunluğu
barkod_uzunlugu = len(barcode)
print("Barkodun uzunluğu:", barkod_uzunlugu)

# barkodda kaç farklı karakter var
farkli_karakterler = set(barcode)
print("Barkodda bulunan farklı karakter sayısı:", len(farkli_karakterler))

# barkoddaki her bir karakterin sayısını bulma
karakter_sayilari = {}
for karakter in barcode:
    if karakter in karakter_sayilari:
        karakter_sayilari[karakter] += 1
    else:
        karakter_sayilari[karakter] = 1

print("Barkodda bulunan her bir karakterin sayısı:")
for karakter, sayi in karakter_sayilari.items():
    print(f"{karakter}: {sayi}")

# İstenilen karakteri bulma
# barcode[starting_index:stopping_index:stepping_size]
barcode[2:8:2]  # 2. indeksten başlayıp 8. indekse kadar 2 adım atarak karakterleri alır
print("2. indeksten başlayıp 8. indekse kadar 2 adım atarak karakterler:", barcode[2:8:2])

barcode[:7:]
print("Barkodun ilk 7 karakteri:", barcode[:7:])

barcode[::3]
print("Barkodun her 3. karakteri:", barcode[::3])

barcode[::]
print("Barkodun tamamı:", barcode[::])

barcode[::-1]
print("Barkodun ters çevrilmiş hali:", barcode[::-1])

barcode.index("g")
print("Karakter 'g' barkodda", barcode.index("g"), "indekste bulunuyor.")