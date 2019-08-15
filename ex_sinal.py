# -*- coding: utf-8 -*-
n1 = int(input("Digite um numero:"))
o = input("Digite um sinal de operação:")
n2 = int(input("Digite outro numero:"))


if o == "+":
	r = n1 + n2
elif o == "-":
	r = n1 - n2
elif o == "/":
	r = n1 / n2
elif o == "*":
	r = n1 * n2
else:
	print ("operação invalida")
print (r)