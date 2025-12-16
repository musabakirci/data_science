def divideNumber(number):
    return number / 2
print(divideNumber(20))

my_list = [10, 20, 30, 40, 50]

myResultlist = []
for num in my_list:
    myResultlist.append(divideNumber(num))
print(myResultlist)

#map fonksiyonu = liste elemanlarına fonksiyon uygulamak için kullanılır
print(list(map(divideNumber, my_list)))

def controlString(string):
    return "Musa" in string
print(controlString("Musa Bakirci"))

myStringList = ["Musa Bakirci", "Ahmet Yılmaz", "Musa", "Mehmet Demir"]
print(list(map(controlString, myStringList)))

#filtreleme = filtreleme yaparak elemanları süzme
print(list(filter(controlString, myStringList)))

#lambda = anonim fonksiyon tanımlamak için kullanılır
multiplyLambda = lambda x: x * 3 # eger bir fonksiyon verilirse bu fonksiyonu 3 ile çarpar
print(multiplyLambda(5))
result = multiplyLambda(10)
print(result)

numlist = [1, 2, 3, 4, 5]
print(list(map(lambda num: num * 3, numlist)))