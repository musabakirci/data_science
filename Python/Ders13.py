from random import randint
from random import shuffle
#range 
my_list = [5,7,9,11,13]
for num in list(range(10)):
    print(num * 2)

print(list(range(5,25,2)))

for num in my_list:
    print(num)

for ix in range(len(my_list)):
    print(f"Index: {ix}, Value: {my_list[ix]}")    

# enumarate 
for element in enumerate(my_list): #burada index ve değer birlikte gelir
    print(element)

for (ix, value) in enumerate(my_list):
    print(f"Value: {value}")

#random
print(randint(1, 100))

#shuffle = karıştırmak
shuffle(my_list)
print(my_list)

print(my_list[randint(0, len(my_list)-1)]) # burada rastgele bir eleman seçilir

#zip
food_list = ["Pizza", "Burger", "Pasta"]
drink_list = ["Coke", "Pepsi", "Water"]
day_list = ["Monday", "Tuesday", "Wednesday"]
meal_combinations = list(zip(food_list, drink_list, day_list))
print(meal_combinations)

new_list = []
my_string = "metallica"

for element in my_string:
    new_list.append(element)
print(new_list)

# list comprehension
new_list = [element for element in my_string]
print(new_list)

number_list = [10, 20, 3, 40, 50]
new_number_list = [num/2 for num in number_list]
print(new_number_list)

new_number_list = []
for num in number_list:
    new_number_list.append(num/2)
print(new_number_list)