# DESAFIO 26
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase=input('Digite a frase:\n').upper()
# Quantas vezes aparece a letra "A"
print(f'Quantas vezes aparece a letra "A"?\nA letra "A" apareceu {frase.count('A')}')
# Em que posição ela aparece a primeira vez
print(f'A letra "A" apareceu a primeira vez na posição {frase.find('A')+1}')
# Em que posição ela aparece a ultima vez
print(f'A letra "A" apareceu a ultima vez na posição {frase.rfind('A')+1}')