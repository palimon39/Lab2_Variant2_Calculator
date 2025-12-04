def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    print("Калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    
    choice = input("Выберите операцию (1, 2 или 3): ")
    
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    if choice == "1":
        result = add_numbers(num1, num2)
        print(f"Сумма: {result}")
    elif choice == "2":
        result = subtract_numbers(num1, num2)
        print(f"Разность: {result}")
    elif choice == "3":
        result = multiply_numbers(num1, num2)
        print(f"Произведение: {result}")
    else:
        print("Неверный выбор")
