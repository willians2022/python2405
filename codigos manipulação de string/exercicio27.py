# DESAFIO 27
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome
# separadamente
# Exemplo: Ana Maria De Souza
# Primeiro: Ana
# Ultimo: Souza

nome=input('digite seu nome:\n').upper().strip()
nomeDividido=nome.split()
print(f'O primeiro nome é: {nomeDividido[0]}')
print(f'O ultimo nome é: {nomeDividido[-1]}')
# ------------------------------------------------
nome1=nome.find(' ')
nome2=nome.rfind(' ')+1
print(f'O primeiro nome é: {nome[:nome1]}')
print(f'O ultimo nome é: {nome[nome2:]}')