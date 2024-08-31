# DESAFIO 31
# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem cobrando R$ 0,50 por Km para
# viagens de até 200 Km e R$ 0,45 para viagens mais longas
# .

distancia=float(input('Digite a distancia da viagem: '))
if distancia <=200:
        valor=distancia*0.5
else:
        valor=distancia*0.45
print(f'O valor da corrida é de R$ {valor:.2f}')