# ввести два числа с консоли и определить какое из них больше
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 > num2:
    print(f"Первое число = {num1} больше чем второе = {num2}")
elif num1 == num2:
    print("num1=num2")
else:
    print(f"Второе  число = {num2} больше чем первое = {num1}")
