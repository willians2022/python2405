# DESAFIO 30
# Crie um programa que leia um número inteiro e mostre na tela se ele
# é PAR ou IMPAR.
numero=int(input('Digite um numero: '))
if numero%2==1:
        print('Ímpar')
else:
        print('Par')
# ------------------------------------------
print('Ímpar' if numero%2==1 else 'Par')