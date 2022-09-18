# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141

import math

d = input("Введите число d")
a = d.split('.')
b = a[1]
res = round(math.pi,len(b))
print()