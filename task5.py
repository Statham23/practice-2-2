# Запрашиваем у пользователя массу и скорость
mass = float(input("Введите массу объекта в килограммах (кг): "))
velocity = float(input("Введите скорость объекта в метрах в секунду (м/с): "))

# Вычисляем кинетическую энергию
kinetic_energy = 0.5 * mass * velocity ** 2

# Выводим результат
print(f"Кинетическая энергия: {kinetic_energy} Дж")