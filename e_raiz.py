import math
def raiz (a, b, c):
    delta = (b * b) - 4 * a * c

    if delta < 0 :
         print('A equação não possui raízes reais')
    elif delta == 0:   
         r_delta = math.sqrt(delta)
         x = (-1 * b + r_delta)/ (2 * a)
         print ('A raiz da equação é %s' %x)
    else:
        r_delta = math.sqrt(delta)
        x = (-1 * b + r_delta)/ (2 * a)
        x2 = (-1 * b - r_delta)/ (2 * a)
        print ('As raizes da equação são %s e %s' %(x, x2))
      