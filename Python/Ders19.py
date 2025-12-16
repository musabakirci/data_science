#inheritance
class Musician():
    def __init__(self,name):
        self.name = name
        print("Musician created")

    def test1(self):
        print("Test 1 executed")

    def test2(self):
        print("Test 2 executed")

musa = Musician("Musa")
print(musa.name)
print(musa.test1())
print(musa.test2())

print("**********")
class Guitarist(Musician):

    def __init__(self, name):
        Musician.__init__(self, name)
        print("Guitarist created")


    def test3(self):
        print("Test 3 executed")

    # Override test1 method
    """
    Override = test1 metoduna yeni bir uygulama eklemektir. BU şekilde yeni eklenen uygulama test1 metodunun
    üzerine yazilmiş olur.
    """
    def test1(self):
        print("Test1, test1, test1")    

kaya = Guitarist("Kaya")
print(kaya.name)
print(kaya.test1())
print(kaya.test2())

print("**********")

kaya.name = "Kaya Bilginer"
print(kaya.name)