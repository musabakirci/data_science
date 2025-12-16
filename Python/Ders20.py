#Polymorphism

class Banana():

    def __init__(self, weight):
        self.weight = weight

    def info(self):
        return "This is a banana and its weight is " + str(self.weight)

class Apple():

    def __init__(self, weight):
        self.weight = weight

    def info(self):
        return "This is an apple and its weight is " + str(self.weight)

banana = Banana(120)
print(banana.info())

apple = Apple(150)
print(apple.info())

print("**********")

fruitList = [banana, apple] #polymorphism
for fruit in fruitList:
    print(fruit.info())