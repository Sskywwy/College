def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Обчислюємо середній індекс
        
        if arr[mid] == target:
            return mid  # Повертаємо індекс, якщо елемент знайдено
        
        elif arr[mid] < target:
            left = mid + 1  # Якщо середній елемент менший за цільовий, шукаємо в правій частині
        
        else:
            right = mid - 1  # Якщо більший, шукаємо в лівій частині
    
    return -1   # Якщо елемент не знайдено

# Приклад використання:
arr = [1, 3, 5, 7, 9]
target = 5
result = binary_search(arr, target)
print(f"Індекс елемента {target}: {result}")

