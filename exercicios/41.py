"""A confederação Nacional de Natação precisa de uma programa que leia
o ano de nascimento de uma atleta e mostre sua categoria, de acordo
com a idade.

Até 9 anos: MIRIM

Até 14 anos: INFANTIL

Até 19 anos: JUNIOR

Até 24 anos: SÊNIOR

Acima: MASTER"""

from datetime import date
ano = int(input('digite o ano de nascimento :'))
mes = int(input('digite o mes do nascimento :'))
dia = int(input('digite o dia de nascimento :'))
aniversario =date(ano,mes,dia)
idade=int((date.today()-aniversario).days/365.2425)
if idade <=3 :
    print ('nao existem uma categoria ')
elif idade <= 9:
    print ('mirim')
elif idade <= 19:
    print ('junior')
elif idade <= 24:
    print ('senior')
else :
    print ('master')