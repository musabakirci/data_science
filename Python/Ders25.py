# Dosya islmeleri

#Dosya olusturma
with open("myfile.txt", "w") as f:
    f.write("Hello, World!")
    f.write("\nWelcome to Data Science Camp 2025.")
    f.write("\nThis is a new line added to the file.")

#Dosyayı açma
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)


with open("myfile.txt", mode="r") as myNewfile2: # r(read) ile acmak dosyayi okuma modunda acar ve icerigini degistirmez.
    myContent = myNewfile2.read()
    
with open("myfile.txt", mode="w") as myNewfile:
    myNewfile.write("This is a new file created.") # w(write) ile acmak yeni bir dosya olusturur ve icerigi degistirip sadece bu dosyayi etkiler önceki her seyi siler.

with open("myfile.txt", mode="a") as myNewfile3: # a(append) ile acmak dosyayi ekleme modunda acar ve icerigini degistirmez sadece sonuna ekleme yapar.
    myNewfile3.write("\nThis line is added later2.")

"""
Olusturdugumuz myfile dosyasinda en üstte belirttigimiz üc ayri paragraf yazar daha sonra w ile dosyayi okuma yapinca en üstte yazdiklarimiz myfile.txt dosyasindan silinir. w den sonraki yerler dosyaya yazilir. w den önceki yerler ise kod calistirildiginda sadece terminalde görülür.
"""