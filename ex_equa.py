# -*- coding: utf-8 -*-
from math import sqrt

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)
x1 = (-b + raiz_delta)/ (2*a)
x2 = (-b - raiz_delta)/ (2*a)

print ("X1 = %d"  %x1)
print ("X2 = %d"  %x2)