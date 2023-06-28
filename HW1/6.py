# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с
# номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

n = str(input("Введите шестизначный номер билета: "))

a = int(n[:3])
b = int(n[3:])
summax = 0
summay = 0

while a > 0 and b > 0:
    x = a % 10
    summax = summax + x
    a = a // 10
    y = b % 10
    summay = summay + y
    b = b // 10
#print(summax)
#print(summay)

if summax == summay:
    print("Поздравляю! У Вас счастливый билет")
else:
    print("Билет не счастливый, попробуйте еще раз :)")