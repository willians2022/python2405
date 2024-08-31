# DESAFIO 37
# Escreva um programa que leia um número inteiro e peça para o usuário
# escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
while True:
    numero=input('Digite um numero para converter: ')
    if numero.isnumeric():
        numero=int(numero)
        menu=input('[1] - Binario\n[2] - Octadecimal\n[3] - Hexadecimal\n\nSelecione: ')
        match menu:
            case '1':
                print(f'{bin(numero).replace('0b','')}')
            case '2':
                print(f'{oct(numero)[2:]}')
            case '3':
                print(f'{hex(numero)[2:]}')
            case _:
                print('Opção invalida!!')