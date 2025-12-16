# Gerekli kütüphanelerin import edilmesi
import numpy as np  # Matematiksel işlemler için
import pandas as pd  # Veri işleme ve analiz için
import matplotlib.pyplot as plt  # Görselleştirme için

# Eğitim ve test veri setlerinin okunması
train_data = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\VerilerKaggle\train.csv")
test_data = pd.read_csv(r"C:\Users\MUSA\Desktop\Veri_Bilimi_Kamp\VerilerKaggle\test.csv")

# Veri setlerinin içeriğinin gösterilmesi
print(train_data)
print("---------------------")

print(test_data)
print("---------------------")

# Veri setleri hakkında bilgi alma (veri tipleri, boş değerler vb.)
print(train_data.info())
print("---------------------")

print(test_data.info())
print("---------------------")

# Sayısal sütunların istatistiksel özeti
print(train_data.describe())
print("---------------------")

print(test_data.describe())
print("---------------------")

# Sütun isimlerinin görüntülenmesi
print(train_data.columns)
print("---------------------")

print(test_data.columns)
print("---------------------")

# Eksik verilerin tespiti (her sütundaki boş değer sayısı)
print(train_data.isnull().sum())
print("---------------------")

print(test_data.isnull().sum())
print("---------------------")

# Kategorik değişkenlerin görselleştirilmesi için fonksiyon tanımı
def degiskenler(variable):
    cat = train_data[variable]  # İlgili değişkenin seçilmesi
    sayi = cat.value_counts()  # Değişkenin değerlerinin frekanslarının hesaplanması
    plt.figure(figsize=(9,5))  # Grafik boyutunun ayarlanması
    plt.bar(sayi.index, sayi)  # Çubuk grafik oluşturulması
    plt.xticks(sayi.index, sayi.index.values)  # X ekseni etiketlerinin ayarlanması
    plt.ylabel("Frequency")  # Y ekseni etiketi
    plt.xlabel(variable)  # X ekseni etiketi
    plt.show()  # Grafiğin gösterilmesi
    print("variable:", variable, "sayi:", sayi)  # Değişken adı ve frekansların yazdırılması

# Kategorik değişkenlerin listesi
category1 = ["Survived","Sex","Pclass","Embarked","SibSp","Parch"]
for i in category1:
    degiskenler(i)  # Her değişken için görselleştirme fonksiyonunun çağrılması
    print("---------------------")

# Benzersiz değer sayısı çok yüksek olan kategorik değişkenlerin analizi
category2 = ["Cabin", "Name", "Ticket"]
for i in category2:
    print(train_data[i].value_counts())  # Her değişkenin değer frekanslarının yazdırılması
    print("---------------------")
    
print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")

# Sayısal değişkenlerin histogram ile görselleştirilmesi için fonksiyon tanımı
def histogram(variable):
    plt.figure(figsize=(9,5))  # Grafik boyutunun ayarlanması
    plt.hist(train_data[variable])  # Histogram oluşturulması
    plt.xlabel(variable)  # X ekseni etiketi
    plt.ylabel("Frequency")  # Y ekseni etiketi
    plt.show()  # Grafiğin gösterilmesi
    print("variable:", variable)  # Değişken adının yazdırılması

# Sayısal değişkenlerin listesi
sayisal = ["Age","Fare", "PassengerId"]
for i in sayisal:
    histogram(i)  # Her değişken için histogram fonksiyonunun çağrılması
    print("---------------------")

# Hayatta kalma oranlarının Pclass'a göre analizi
survived = train_data[["Pclass", "Survived"]].groupby(["Pclass"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print(survived)
print("*********************")

# Hayatta kalma oranlarının Cinsiyete göre analizi
survived = train_data[["Sex", "Survived"]].groupby(["Sex"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print(survived)
print("*********************")

# Hayatta kalma oranlarının Kardeş/Eş sayısına göre analizi
survived = train_data[["SibSp", "Survived"]].groupby(["SibSp"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print(survived)
print("*********************")

# Hayatta kalma oranlarının Ebeveyn/Çocuk sayısına göre analizi
survived = train_data[["Parch", "Survived"]].groupby(["Parch"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print(survived)
print("*********************")

# Eksik verilerin doldurulması işlemleri
train_data_len = len(train_data)  # Eğitim veri setinin uzunluğunun kaydedilmesi
# Eğitim ve test veri setlerinin birleştirilmesi
train_data1 = pd.concat([train_data, test_data], axis=0).reset_index(drop=True)
print(train_data1)
print("---------------------")

# Eksik değer içeren sütunların tespiti
print(train_data1.columns[train_data1.isnull().any()])
print("---------------------")

# Eksik değerlerin toplam sayısı
print(train_data1.isnull().sum())
print("---------------------")

# Yaş değeri eksik olan kayıtların gösterilmesi
print(train_data1[train_data1["Age"].isnull()])
print("---------------------")

# Biniş limanına göre ücret dağılımının kutu grafik ile gösterilmesi
train_data1.boxplot(column="Fare", by="Embarked")
plt.show()

# Eksik Embarked değerlerinin 'C' (Cherbourg) ile doldurulması
train_data1["Embarked"] = train_data1["Embarked"].fillna("C")
print(train_data1["Embarked"])

# Eksik değerlerin güncel durumunun kontrol edilmesi
print(train_data1.isnull().sum())
print("---------------------")