#Abstraction
"""
Abstraction, karmaşik sistemlerin basitleştirilmesi ve sadece gerekli bilgilerin sunulmasidir.
Bu, kullanicilarin veya diger sistemlerin sadece gerekli detaylara erisebilmesini saglar ve gereksiz detaylari gizler.
"""

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def max_speed(self):
        pass

class Tesla(Car):
    def max_speed(self):
        print("Max speed is 250 km/h")

    def battery_range(self):
        print("Battery range is 400 km")

class BMW(Car):
    def max_speed(self):
        print("Max speed is 240 km/h")

    def battery_range(self):
        print("Battery range is 450 km")

tesla = Tesla()
tesla.battery_range()
tesla.max_speed()

print("-------------------------")

bmw = BMW()
bmw.battery_range()
bmw.max_speed()
