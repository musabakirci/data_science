# Özel Methodlar

class Fruit():

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    #Özel Methodlar => Googledan python special methods list diye aratabiliriz.
    def __str__(self):
        return f"{self.name} has {self.calories} calories."
    
    def __len__(self):
        return self.calories
    
myFruit = Fruit("Apple", 95)
print(myFruit)
print(len(myFruit))

print("-------------------------")

class Train():
    def __init__(self, name):
        self.name = name

    def __getitem__(self, key):
        if key == "a":
            return self.name
        else:
            return "Not Found"

myTrain = Train("Express")
print(myTrain["a"])
print(myTrain["b"])