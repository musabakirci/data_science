mySuperHero = "Spider-Man"
print(mySuperHero)

print(mySuperHero=="Spider-Man")

if mySuperHero == "Spider-Man":
    print("My superhero is Spider-Man!")
elif mySuperHero == "Batman":
    print("My superhero is Batman!")
elif mySuperHero == "Superman":
    print("My superhero is Superman!")
else:
    print("My superhero is not Spider-Man.")

print("***********************")

Age = int(input("Please enter your age: "))

if Age < 18:
    print("You are a minor.")
elif Age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

MySuperHero = input("Please enter your superhero name: ")    
my_superhero_list = ["Spider-Man", "Batman", "Superman"]

if MySuperHero in my_superhero_list:
    print(f"My superhero is {MySuperHero}!")
else:
    print("My superhero is not in the list.")
