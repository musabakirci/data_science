# for loop, while loop
# for loop

my_list = [10, 20, 30, 40, 50]
print(my_list[0]/5*2)
print(my_list[1]/5*2)

for item in my_list:
    print(item/5*2)

print("*************************")

for x in my_list:
    new_number = x/5*2
    print(new_number)
print("for loop ended")

print("*************************")

for number in my_list:
    if number % 6 == 0:
        print(f"{number} is divisible by 6.")
    else:
        print(f"{number} is not divisible by 6.")

print("*************************")

MyString = "Bilgi İşlem Daire Başkanligi"

for k in MyString:
    print(k)

print("**************************")

my_tuple = (10, 20, 30, 40, 50)

for num in my_tuple:
    print(num / 5 * 2)

print("*************************")

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

print("********************")

my_new_liste = [("a","b"), ("c","d"), ("e","f"),("g","h")]
print(len(my_new_liste))


print("********************")

for element in my_new_liste:
    print(element)

print("********************")

#tuple unpacking

for (a, b) in my_new_liste:
    print(f"First element: {a}, Second element: {b}")
    print("Alone is " + a)
    print("Second lone is " + b)

my_dictionary = {"k1":100,"k2":200,"k3":300}
for element in my_dictionary:
    print("Key is " + element)
    print("Value is " + str(my_dictionary[element]))

my_dictionary.items()  # Bu metot, sözlüğün anahtar-değer çiftlerini döndürür.
for key, value in my_dictionary.items():
    print("Key is " + key)
    print("Value is " + str(value))