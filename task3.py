# Запрашиваем у пользователя температуру в градусах Фаренгейта
fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))

# Переводим температуру в градусы Цельсия
celsius = (fahrenheit - 32) * 5 / 9

# Выводим результат
print(f"Температура в градусах Цельсия: {celsius:.2f}