#1
num = int(input("Введіть число: "))
if num > 5:
    print("Більше 5")
elif num == 5:
    print("Дорівнює 5")
else:
    print("Меньше  5")

#2
num = int(input("Введіть число: "))
if num > 10:
    print("Більше 10")
    
if num > 20:
    print("Більше 20")

if num == 100:
    print("Велике число")

#3

BirthYear = int(input("Введіть рік народження: "))
Age = int(2023 - BirthYear)
if Age < 10:
    print("Ви ще дитина")
    
if Age > 10 and Age < 18:
    print("Ви підліток")

if Age > 18 and Age < 60:
    print("Ви доросла людина")
    
if Age < 0 or Age > 100:
    print("Ввели неправельний вік народження")
#4
Num = int(input("#4  5Введіть число: "))
if  Num != 7:
    print("Не 7")
else:
    if not Num == 8:
        print("Так 7")
        
#5
text = input("Ввести текст: ")
if text == "Екзамен":
    exam = True
else:
    exam = False
    
if exam == True:
    print("здав")

if exam == False:
    print("Не здав")