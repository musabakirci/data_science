# Hatalari Ele Almak

#try-except
while True: 
    try:
        myAge = int(input("Enter your age: "))
        print("Your age is:", myAge*2)

    except:
        print("Invalid input! Please enter a number.")


    else: # Bu blok hata oluşmadığında çalışır
        print("Else executed")
        break

    finally: # finally bloğu her durumda çalışır
        print("Finally executed")
"""
Cogu zaman hata ayiklama sirasinda else ve finally kullanilmaz. break try'in altinda kullanilir ve yeterlidir.
"""


