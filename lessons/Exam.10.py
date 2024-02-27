# 1.*Підрахунок середнього значення*: Створіть функцію, яка приймає список чисел і повертає середнє арифметичне цих чисел.
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Приклад використання:
numbers = [1, 2, 3, 4, 5]
print("Середнє значення:", average(numbers))

# 2.*Перевірка на простоту*: Напишіть функцію, яка приймає число і перевіряє, чи є воно простим. Використайте лямбда-функцію для перевірки кожного можливого дільника числа.
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def check_prime(num):
    if is_prime(num):
        return f"{num} є простим числом"
    else:
        return f"{num} не є простим числом"

# Приклад використання:
number = 17
print(check_prime(number))

# 3.*Генерація паролю*: Створіть функцію, яка генерує випадковий пароль заданої довжини. Використовуйте можливості як звичайних функцій, так і лямбда-функцій для генерації різних частин паролю (букви верхнього і нижнього регістрів, цифри, спеціальні символи).
import random
import string

def generate_password(length):
    # Символи, які можуть бути в паролі
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генеруємо пароль з випадкових символів довжиною length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Приклад використання:
password_length = 10
print("Згенерований пароль:", generate_password(password_length))