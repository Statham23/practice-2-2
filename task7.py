# Запрашиваем у пользователя силу и площадь
force = float(input("Введите силу в ньютонах (N): "))
area = float(input("Введите площадь в квадратных метрах (м²): "))

# Вычисляем давление
pressure = force / area

# Выводим результат
print(f"Давление: {pressure} Па")