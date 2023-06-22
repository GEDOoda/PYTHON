# num = int(input("Введите целое натуральное число: "))
# i = 1
# faktorial = 1
# while i <= num:
#     faktorial *= i
#     i = i + 1
# else:
#     print(f"Факториал числа {num} равен {faktorial}")


#Дано натуральное число А > 1. Определите каким числом по счету фибоначи оно является. Если не является числом фиббоначи то выведите -1.

# num = int(input("Введите ваше число: "))
# fnum1 = 1
# fnum2 = 1
# sum = 1
# count = 2
# while fnum2 < num:
#     sum = fnum1 + fnum2
#     fnum1 = fnum2
#     fnum2 = sum
#     count += 1
    
# if fnum2 == num:
#     print(count)
# else:
#     print(-1)

# from random import randint
# days,count = int(input("Введите какое количество дней рассматриваем: ")),0
# for grad in range (days):
#     grad = randint(-3, 3)
#     print(grad)
#     if grad > 0:
#         count +=1
# print(f"{count} дня было тепло")

#Купить нужно два арбуза один тяжелый и один легкий. Арбузов несколько. Напишите программу которая поможет в решении.

# from random import randint
# kol = int(input("Введите кол-во арбузов: "))
# i = 0
# max , min = 0, 15
# while i < kol:
#     mass = randint(5, 15)
#     print(mass, end =  " ")
#     if min > mass:
#         min = mass
#     if max < mass:
#         max = mass
#     i += 1

# print(f"Тяжелый арбур весит {max} а легкий арбуз весит {min}")

