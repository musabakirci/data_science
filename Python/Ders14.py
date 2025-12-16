# Method vs Function
my_name = "Musa"
print("My name is " + my_name)

my_name = my_name.upper()
print("My name is " + my_name)

#functions
def hello_python():
    print("Hello Python")
    print("Hello again")

hello_python()

def hello_name(name):
    print("Hello " + name)

hello_name("Ali MİRAN")
hello_name("Ayşe YILMAZ")

def sumExample(a, b):
    print(a + b)

sumExample(5, 10)

def sumExample2(a, b, c):
    print(a + b + c)

sumExample2(5, 10, 15)

def Hello_surname(surname="Kaya"):
    print("Hello " + surname)

Hello_surname("Bakırcı") # bu şekilde biz belirtirsek değer "Bakırcı"
Hello_surname() # burada ise varsayılan değer "Kaya" kullanılır