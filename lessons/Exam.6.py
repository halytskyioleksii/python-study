#1. Створіть програму, яка приймає від користувача рядок тексту і визначає найбільше слово у цьому тексті, виводячі його.
user_text = input("Введіть рядок тексту: ")
words = user_text.split()
longest_word = max(words, key=len)
print("Найбільше слово:", longest_word)

#2. Напишіть програму, яка приймає від користувача рядок та виводить його зі словами, виведеними в звородньому напрямку.
user_input = input("Введіть рядок: ")
reversed_words = ' '.join(word[::-1] for word in user_input.split())
print("Рядок з реверсованими словами:", reversed_words)

#3. Напишіть програму, яка замінює всі групи букв "а", "б", "в" у введеному рядку на відповідні числа "1", "2", "3", використовуючи індексацію та зрізи для перевірки кожного символу.
input_str = input("Введіть рядок: ")
modified_str = ""
for char in input_str:
    if char.lower() == 'а':
        modified_str += '1'
    elif char.lower() == 'б':
        modified_str += '2'
    elif char.lower() == 'в':
        modified_str += '3'
    else:
        modified_str += char

print("Змінений рядок:", modified_str)
