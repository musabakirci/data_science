#key-value pairing
fruit_list = ["apple", "banana", "cherry"]
calorie_list = [95, 105, 77]

fitness_dictionary = {"banana": 105, "apple": 95, "cherry": 77}

print("Fitness dictionary:", fitness_dictionary)
print(type(fitness_dictionary))
print(fitness_dictionary["banana"])

print(fitness_dictionary.keys()) 
print(fitness_dictionary.values())

fitness_dictionary["banana"] = 110
print("Updated fitness dictionary:", fitness_dictionary)

fitness_dictionary["orange"] = 80
print("Fitness dictionary after adding orange:", fitness_dictionary)

my_dictionary = {44:"Malatya", 23:"Elazığ", 34:"Istanbul"}
print(my_dictionary[34])  # "Istanbul" değerini alır

my_mixed_dictionary = {"Malatya": [44, 58, 45], "Elazığ": 23, "Istanbul": 34}
print(my_mixed_dictionary["Malatya"][1])  # "Malatya" anahtarının değerindeki listenin 1. indeksini alır

last_dictionary = {"k1":10, "k2":[10, 20, 30, 40], "k3":"string","k4":{"a":115, "b":225}}
print(last_dictionary["k4"]["b"])  # "k4" anahtarının değerindeki sözlüğün "b" anahtarının değerini alır
print(last_dictionary["k2"][2])  # "k2" anahtarının değerindeki listenin 2. indeksini alır