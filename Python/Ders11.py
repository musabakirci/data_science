# continue - break - pass
mylist = [10, 20, 30, 40, 50, 60, 70]
for num in mylist:
    print(num)
print("Bitti")
print(40 in mylist)
print("*************************")
for number in mylist:
    print(number)
    if number == 40:
        print("Durdu...")
        break
print("*************************")
for number in mylist:
    if number == 40:
        continue
    print(number)
print("*************************")
for number in mylist:
    pass