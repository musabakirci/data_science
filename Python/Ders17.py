# Scope (LEGB)
from unittest import removeResult


x = 20   # Global değişken

def multiply(num):
    x = 10   # Local değişken (sadece bu fonksiyon içinde geçerli)
    return x * num

print("multiply(5):", multiply(5))  # 10 * 5 = 50


# LEGB -> Local, Enclosing, Global, Built-in

# Global scope
my_string = "Miran"

def myFunction():
    # Enclosing scope
    my_string = "Miran2"

    def myFunction2():
        # Local scope
        my_string = "Miran3"
        print("Local:", my_string)

    myFunction2()  # iç fonksiyonu çağırıyoruz
    print("Enclosing:", my_string)

print("Global:", my_string)
myFunction()
print("Global (tekrar):", my_string)


myVariable = 10
def test1():
    print(myVariable * 2)

def test2():
    print(myVariable * 3)

test1()
test2()    
''' myVariable her iki fonksiyonun üstünde olduğu için kodlari calistirinca her iki fonksiyon calisir'''



def test3():
    my_variable = 5
    print(my_variable * 2) # fonksiyon calisir cünkü degisken bu fonksiyon içinde tanımlı

#def test4():
    #print(my_variable * 3) # hata verir çünkü my_variable bu fonksiyonun içinde tanımlı değil


y = 10
def newFunction(y):
    print(y)
    y = 5
    print(y)
    return y

newFunction(10)

y = 10
def ChangeY():
    global y  # global anahtar kelimesi ile global değişkeni kullanıyoruz
    y = 5
    print("Inside ChangeY:", y)
ChangeY()    
print("Outside ChangeY:", y)  # global değişkenin değeri değişti