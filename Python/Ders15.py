#return
def summation(num1, num2, num3):
    print(num1 + num2 + num3)

summation(10,5,12)

x = summation(10,5,12)
print(x) # None döner çünkü return yok

def return_summation(num1, num2, num3):
    result = num1 + num2 + num3
    print("Function içinde: ", result)
    return result

x = return_summation(10, 15, 23)


def control_string(s):
    if s[0]=="a":
        print("String 'a' ile başlıyor.")
    else:
        print("String 'a' ile başlamıyor.")

control_string("atlantis")        
control_string("Kanada")

#args, kwargs (arguments, key word arguments)

#args= birden fazla argüman göndermeye yarar.

def args_sum(*args):
    return sum(args)
print(args_sum(10, 20, 30, 40, 50))

def args_example(*args):
    print("Arguments: ", args)
args_example(123,125,126,341)


#kwargs= anahtar kelime argümanları, isimli argümanlar göndermeye yarar.
def kwargs_example(**kwargs):
    print(kwargs)
kwargs_example(apple = 5, banana = 10, cherry = 15)

def kwargs_example2(**kwargs):
    if "apple" in kwargs:
        print("Apple found:", kwargs["apple"])
    else:
        print("Fruit not found")

kwargs_example2(apple = 5, banana = 10, cherry = 15)        
kwargs_example2(melon = 20)