def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

if __name__ == "__main__":
    print("Калькулятор")

cat > calc.py << 'EOF'
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

if __name__ == "__main__":
    print("Калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    choice = input("Выберите операцию (1-4): ")
    
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
    elif choice == "4":
        result = divide_numbers(num1, num2)
        print(f"Частное: {result}")
    else:
        print("Неверный выбор")
