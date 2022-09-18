# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

N = int(input("Введите число N "))
list = []
i = 2

if (N == 1):
    list.append(1)
else:
    while N > 1:
        if ((N % i) != 0):
            i+=1
        else:
            N = N / i
            list.append(i)

print(list)