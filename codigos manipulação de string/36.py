# DESAFIO 38
# Escreva um programa que leia dois números inteiros e compare- os,
# mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero1=int(input('Digite um numero: '))
numero2=int(input('Digite um numero: '))

if numero2==numero1:
    print(f'O maior numero é o {max(numero1,numero2)}')
else:
    print(f'Os numeros são iguais. numero: {numero1}')