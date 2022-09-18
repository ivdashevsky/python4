# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input("Введите число k: "))

list_degree = []
list_item = []
res = ''


for i in range(k, -1, -1):
    list_degree.append(str(i))
    list_item.append(str(randint(0,5)))
    

for i in range(len(list_degree)):
    if (i != len(list_degree)-1):
        if ((list_item[i] != '0') & (list_item[i] != '1')):
            res += list_item[i] + '*x^' + list_degree[i] + ' + '
        if (list_item[i] == '1'):
            res += 'x^' + list_degree[i] + ' + '
        else:
            res += ''
    else:
        if (list_item[i] == '0'):
            res += ''
        else:
            res += list_item[i] + ' = 0'

print(list_degree,list_item)
print(res)

with open('test.txt','w') as data:
    data.write(res)