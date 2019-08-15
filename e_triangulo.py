def triangulo(a, b, c):
    lado1 = a + b
    lado2 = a + c
    lado3 = b + c 

    if a > lado3 or b > lado2 or c > lado1  :
        print ('Não é um triângulo') 
    else:
        print ('É um triângulo')