# Завдання 1 Створіть кортеж, що містить назви місяців у річному циклі та виведіть його.
months = ('Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень')
print(months)

# Завдання 2 Створіть два кортежі, об'єднайте їх та виведіть результат.
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# Завдання 3. Створіть кортеж, що містить ім'я, вік та стать кожної людини в вашому списку друзів. Потім виведіть цей кортеж для кожного друга.
info = ('Ім\'я', 'Вік', 'Місто')
print(info[0])  # Виведення ім'я
print(info[1])  # Виведення віку
print(info[2])  # Виведення міста

# Завдання 4. Напишіть функцію, яка приймає кортеж чисел та повертає його мінімальне і максимальне значення.
def min_max(numbers):
    return min(numbers), max(numbers)

numbers = (5, 6, 12, 8, 1, 4)
min_value, max_value = min_max(numbers)
print("Мінімальне значення:", min_value)
print("Максимальне значення:", max_value)