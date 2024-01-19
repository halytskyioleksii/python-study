num = int(input("Enter num: "))

isHasCar = True
# ==, !=, <, >, =, >=
if num >= 55 or not isHasCar:
    print("Yes")
    if num == 100:
        print("Num is 100")
elif num == 40:
    print("Num is 40")
else:
    print("Else")
    
isHappy = True
if not isHappy:
    print("Yes, he is happy")

print("More text")


data = 'Info'
#if data == 'Info':
#   correct = True
#else:
#   correct = False
 
correct = True if data == 'Info' else False
   
print(correct)