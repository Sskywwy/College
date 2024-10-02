# Функція для видалення повторюваних елементів
def remove_duplicates(input_list):
    # Використаємо множину для унікальних значень та повернемо їх як список
    return list(set(input_list))

# Функція для сортування списку
def sort_mixed_list(input_list):
    # Створюємо два окремі списки для чисел та рядків
    numbers = []
    strings = []
    
    # Розділяємо числа та рядки
    for item in input_list:
        if isinstance(item, (int, float)):  # Якщо це число
            numbers.append(item)
        elif isinstance(item, str):  # Якщо це рядок
            strings.append(item)
    
    # Сортуємо числа і рядки
    numbers.sort()
    strings.sort()
    
    # Об'єднуємо списки: спочатку числа, потім рядки
    return numbers + strings

# Початковий список
original_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
set(original_list)
print (original_list)
# Видаляємо повторювані елементи
unique_list = remove_duplicates(original_list)
print("Список без повторень:", unique_list)

# Сортуємо список
sorted_list = sort_mixed_list(unique_list)
print("Відсортований список:", sorted_list)
