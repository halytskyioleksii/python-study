# 1. Створіть програму, яка відкриває текстовий файл для читання за допомогою менеджера "with...as" і виводить його вміст на екран. Впевніться, що програма правильно обробляє винятки, такі як відсутність файлу.
try:
    with open('file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не знайдено.")
except Exception as e:
    print("Сталася помилка:", e)
    
# 2. Створіть програму, яка відкриває текстовий файл для читання за допомогою менеджера "with...as" і виводить його вміст на екран. Впевніться, що програма правильно обробляє винятки, такі як відсутність файлу.
def write_to_file(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print("Рядки були успішно записані у файл", file_path)
    except Exception as e:
        print("Сталася помилка під час запису у файл:", e)

# Приклад виклику функції:
lines = ["Рядок 1", "Рядок 2", "Рядок 3"]
write_to_file('output.txt', lines)

# 3. Створіть програму, яка копіює вміст одного текстового файлу у інший, використовуючи менеджер "with...as" для обох файлів. Переконайтеся, що в програмі передбачено обробку винятків, таких як відсутність вихідного файлу чи помилки під час копіювання.
def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
            for line in source_file:
                destination_file.write(line)
        print("Файл успішно скопійовано.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка під час копіювання:", e)

# Приклад виклику функції:
copy_file('source.txt', 'destination.txt')
