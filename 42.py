# DESAFIO 42
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes


reta1 = int(input('digite o valor da 1° reta :' ))
reta2 = int(input('digite o valor da 2° reta :' ))
reta3 = int(input('digite o valor da 3° reta :' ))

if reta1+reta2>reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    if reta1 == reta2 == reta3:
        print(f'triangulo equilatero')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1 :
        print('triangulo isosceles')
    else:
        print('escaleno todos os lados diferente ')
else:
    print('não forma um triangulo')