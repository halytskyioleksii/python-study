number = int(input("Введіть число: "))

if number > 9:
    result = number ** 2
    print("В ступені 2: ")
else:
    result = number ** 4 
    print("В ступені 4: ")
print(result)