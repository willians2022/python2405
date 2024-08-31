# DESAFIO 42
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

reta1=int(input('Digite o valor da 1º reta: '))
reta2=int(input('Digite o valor da 2º reta: '))
reta3=int(input('Digite o valor da 3º reta: '))
if reta1+reta2>reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    # Equilátero: Todos os lados iguais
    if reta1==reta2==reta3:
        print('Equilátero: Todos os lados iguais')
    # Isósceles: Dois lados iguais
    elif reta1==reta2 or reta2==reta3 or reta3==reta1:
        print('Isósceles: Dois lados iguais')
    # Escaleno: Todos os lados diferentes
    else:
        print('Escaleno: Todos os lados diferentes')
else:
    print('Não pode formar um triangulo')