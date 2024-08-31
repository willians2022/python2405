# DESAFIO 39
# Faça um programa que leia o ano de nascimento de um jovem e
# informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou o tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou
# do prazo.
from datetime import date  #pois vamos utilizar apenas a data sem a hora
ano=int(input('Digite o ano do seu nascimento: '))
mes=int(input('Digite o mes do seu nascimento: '))
dia=int(input('Digite o dia do seu nascimento: '))
aniversario=date(ano,mes,dia)
idade= int((date.today()-aniversario).days/365.2425)
if idade > 18:
    print(f'Já passou da hora de se alistar. Passou {idade-18} anos')
elif idade < 18:
    print(f'Ainda vai alistar. em {18-idade} anos')
else:
    print('Está na hora de se alistar')