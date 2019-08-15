def calcula_imc(peso, altura):
    try:
        imc = peso / (altura * altura)

        if imc < 16:
            print ('Magreza grave')
        elif imc > 16 and imc < 17:
            print ('Magreza moderada')
        elif imc > 17 and imc < 18.5:
            print ('Magreza leve')
        elif imc > 18.5 and imc <25:
            print ('Saudável')
        elif imc > 25 and imc <30:
            print ('Sobrepeso')
        elif imc > 30 and imc <35:
            print ('Obesidade Grau I')
        elif imc > 35 and imc <40:
            print ('Obesidade Grau II')
        else:
            print ('Obesidade Grau III')  
    except: 
        print('Valor inválido')
 

    