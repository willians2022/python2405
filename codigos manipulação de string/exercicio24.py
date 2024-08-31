# DESAFIO 24
# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome "Santo“.


cidade=input('Digite o nome da cidade: ').upper()
primeiroNome=cidade.split()[0]
print(f"começa ou não com o nome 'Santo'?\n{'SANTO' in primeiroNome}")
# ----------------------------------------------------------------------------
print(f"começa ou não com o nome 'Santo'?\n{'SANTO' in cidade[:6]}".upper())