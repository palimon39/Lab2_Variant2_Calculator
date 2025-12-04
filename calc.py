def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = add_numbers(num1, num2)
    print(f"Сумма: {result}")
