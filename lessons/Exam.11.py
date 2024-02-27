# 1.*Читання файлу із списком імен*: Напишіть програму, яка читає файл зі списком імен робітників (кожне ім'я на окремому рядку) і виводить на екран кількість робітників у списку.
def count_names(filename):
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
            print("Кількість робітників:", len(names))
    except FileNotFoundError:
        print("Файл не знайдено!")

# Приклад використання:
count_names("employees.txt")

# 2.*Збереження до файлу*: Створіть програму, яка дозволяє користувачеві ввести кілька рядків тексту, а потім зберігає цей текст у файлі на диску.
def save_to_file(filename):
    try:
        with open(filename, 'w') as file:
            text = input("Введіть текст для збереження у файлі: ")
            file.write(text)
        print("Текст успішно збережено у файлі", filename)
    except:
        print("Виникла помилка при збереженні у файл!")

# Приклад використання:
save_to_file("saved_text.txt")

# 3.*Аналіз лог-файлу*: Напишіть програму, яка аналізує лог-файл сервера і виводить на екран кількість запитів, які здійснювалися певного дня (користувач вказує дату), а також список унікальних IP-адрес, з яких були здійснені ці запити.
def analyze_log_file(log_file, date):
    requests_count = 0
    unique_ips = set()
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if date in line:
                    requests_count += 1
                    parts = line.split()
                    ip_address = parts[0]
                    unique_ips.add(ip_address)
        print("Кількість запитів за", date, ":", requests_count)
        print("Унікальні IP-адреси:", unique_ips)
    except FileNotFoundError:
        print("Файл логів не знайдено!")

# Приклад використання:
analyze_log_file("server_log.txt", "2024-02-26")