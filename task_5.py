print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

# Вариант без цикла
ticket = int(input('Введите номер билета: '))

part1 = (ticket // 1000)
part2 = ticket % 1000

part1 = part1 // 100 + (part1 // 10) % 10 + part1 % 10
part2 = part2 // 100 + (part2 // 10) % 10 + part2 % 10

if part1 == part2:
	print('Билет счастливый!')
else:
	print('Билет не счастливый!')

# # # Вариант с циклом
# ticket = int(input('Введите номер билета: '))
# part1 = part2 = 0
# count_middle = 0

# while ticket > 0:
#   count_middle += 1
#   if count_middle <= 3:
#     part1 += ticket % 10
#   else:
#     part2 += ticket % 10

#   ticket //= 10

# if part1 == part2:
#   print('Билет счастливый!')
# else:
#   print('Билет не счастливый!')
