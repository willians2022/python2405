# DESAFIO 3
# Crie um programa que leia o nome de uma pessoa e diga se
# ela tem "Silva" no nome

nome=input('Digite o nome: ').lower().strip()
print(f'tem "Silva" no nome ?\n{'silva' in nome}')