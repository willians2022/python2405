from random import randint as rd

pc=rd(0,5)
print(pc)
jogada=int(input('Digite um numero entre 0 e 5: '))
if pc == jogada:
    print('Acertou')
else:
    print('Errou')