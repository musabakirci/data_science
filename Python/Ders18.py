#class
'''
Yazacagimiz kodu daha moduler hale getirmek icin siniflar olusturacagiz.
Siniflar, benzer verileri ve fonksiyonlari bir arada tutmamizi saglar.
Siniflar, nesne tabanli programlamanin temelini olusturur.
Sinif adlari genellikle buyuk harfle baslar.
'''
class Person:
    name = ""
    age = 0
    gender = ""

    #constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

musa = Person("Musa", 23, "Erkek")
print(musa.name)
print(musa.age)
print(musa.gender)

class Dog():
    year = 7  # class variable
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.dogHumanAge = age * self.year

    def humanAge(self):
        return self.age * self.year # Dog.year=self.year

myDog = Dog("Karabas", 3, "Kangal")
print(myDog.name)
print(myDog.age)
print(myDog.breed)
print(myDog.humanAge())
print(myDog.dogHumanAge)