# Робота з текстом
word = list('itproger')
word[0] = 'I'
word.append('!')
result = ','.join(word)
# print(result.capitalize())
# print(result.islower())

text = 'football,basketball,skate'
hobbies = text.split(',')

for i in range(0, len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()

result = ",".join(hobbies)
print(result)

# Індекси та зрізи
lis = [5, 3, True, "Some", [5, 4]]
print(lis[:-4:-1])