# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть


from random import randint
countN = int(input("Введите число монеток: "))
tails = 0
eagle = 0
count = 0
for i in range(countN):
    n = randint(0, 1)
    if n == 0:
        eagle += 1
    else:
        tails += 1
    print(n)
if eagle >= tails:
    count = countN - eagle
else:
    count = countN - tails
print('Минимальное количество монет', count)