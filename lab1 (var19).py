#math
x=float(input('Введите x: '))
import math
z=(1-2*(math.sin(x)**2))/(1+(math.sin(x)**2))
print (z)
#vid a do b
def sum_even(a, b):
    if (a % 2 == 1):
        a += 1
    if (b % 2 == 1):
        b -= 1
    return a * (0.5 - 0.25 * a) + b * (0.25 * b + 0.5)
a=float(input('Введите a: '))
b=float(input('Введите b: '))
print(sum_even(a, b))
#massiv
mlist = [int(h) for h in input('Введите значения через пробел ').split()]
print(min(([h for h in mlist if h>0])))
print(sum(([h for h in mlist if h%3 and h>0 ]))) #nikak ne mogy pofixit' kratnost'

print([h for h in mlist if h!=0])