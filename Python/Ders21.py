#Encapsulation 

class Phone():
    def __init__(self, battery, price, name):
        self.__battery = battery
        self.__price = price
        self.__name = name

        """
        İki çizgi (__) koyunca bu değişkenler disaridan erişilemez olur.
        """

    def info(self):
        print(f"Phone name: {self.__name}, Price: {self.__price}, Battery: {self.__battery}")

    # Fiyatı değiştiren metod
    def changePrice(self, price):
        self.__price = price

iphone = Phone(70, 15000, "Iphone14")
iphone.info()

iphone.changePrice(400)
iphone.info()