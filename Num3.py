# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

list_n = input("Введите последовательность чисел через пробел: ").split()
print(list_n)
N = len(list_n)

for i in range(N):
    list_n[i] = int(list_n[i])

list_n.sort()

print(list_n)

list_delete = []

for i in range(0,N-2):
    if ((list_n[i] == list_n[i+1]) & (list_n[i] not in list_delete)):
        list_delete.append(list_n[i])

print(list_delete)