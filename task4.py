# Запрашиваем у пользователя силу и расстояние
force = float(input("Введите силу в ньютонах (N): "))
distance = float(input("Введите расстояние в метрах (m): "))

# Вычисляем работу
work = force * distance

# Выводим результат
print(f"Работа: {work} Дж")