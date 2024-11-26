def main():
    while True:
        print("Выберите задачу (или нажмите 'q' для выхода):")
        print("1. Задача 1")
        print("2. Задача 2")
        print("3. Задача 3")

        choice = input("Введите номер задачи: ")
        if choice == "q":
            print("Выход из программы...")
            break
        elif choice == "1":
            print("Вы выбрали задачу 1")
        elif choice == "2":
            print("Вы выбрали задачу 2")
        elif choice == "3":
            print("Вы выбрали задачу 3")
        else:
            print("Неверный выбор. Попробуйте снова.")

if name == "main":
    main()