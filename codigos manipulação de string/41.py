# DESAFIO 41
# A confederação Nacional de Natação precisa de uma programa que leia
# o ano de nascimento de uma atleta e mostre sua categoria, de acordo
# com a idade.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER
from datetime import date

ano=int(input('Digite o ano de nascimentoo: '))
mes=int(input('Digite o mes de nascimentoo: '))
dia=int(input('Digite o dia de nascimentoo: '))
aniversario=date(ano,mes,dia)
idade= int((date.today()-aniversario).days/365.2425)

if idade<=3:
    print('Não existe uma categoria')
# Até 9 anos: MIRIM
elif idade <=9:
    print('MIRIM')
# Até 14 anos: INFANTIL
elif idade <=14:
    print('INFANTIL')
# Até 19 anos: JUNIOR
elif idade <=19:
    print('JUNIOR')
# Até 24 anos: SÊNIOR
elif idade <= 24:
    print('SÊNIOR')
# Acima: MASTER
else:
    print('MASTER')