#Цикл for
for i in range(5, 21, 2):
    print("El: ", i)

print("\n\n\n\n")

word = 'Some text'
for i in word:
    print(i)

word = 'Some text'
for i in word:
    if i == "m":
        print("Літера m є у слові")

#Цикл while
i = 0
while i <= 10:
    print(i)
    i += 1

work = True
while work:
    user_input = input("Enter word STOP: ")
    if user_input == 'STOP':
        work = False
print("While loop is done")

for i in range(200):
    
    if i % 2 == 0:
        continue
    
    if i == 7:
        break
    
    print("El: ", i)
    
#Else в циклі
for i in "Hello world":
    if i == 'l':
        print("Done")
        break
else:
    print("Not found")