user_hobby = int(input("Скільки у вас всього хобі: "))

i = 0
hobby = []
while i < user_hobby:
    text = "Хобі номер: " + str(i + 1) +":"
    hobby.append(input(text))
    
    i += 1

print(hobby)
