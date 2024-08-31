# DESAFIO 29
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

# variavel que recebe um numero inteiro

velocidade=int(input('Digite a velocidade: '))

# se variavel é maior que 80
if velocidade > 80:
    (variavel - 80) * 7
if velocidade < 87:
    print(f'Você foi multado em R${(velocidade-80)*7:,.2f}')