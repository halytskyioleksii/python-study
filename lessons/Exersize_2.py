someNumber = int(input("Введіть сюди число: "))
if someNumber <= 0:
    print("Число повинно бути меньше 0")
else:
    for i in range(0, someNumber, 2):
        i = i + 1
        print(i)
        