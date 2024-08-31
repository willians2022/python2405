# DESAFIO 36
# Escreva um programa para aprovar um empréstimo bancário para a
# compra de uma casa. O programa vai perguntar o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.
valordacasa=float(input('Digite o valor da casa:\n'))
salario=float(input('Digite o valor do salario:\n'))*0.3 #recebendo 30% do salario
tempoFinanciamneto=int(input('Digite o tempo de financiamneto:\n'))*12 #tranformando os anos em meses
parcela=valordacasa/tempoFinanciamneto
if parcela < salario:
    print(f'Emprestimo aprovado. O valor da parcela ficara {parcela:,.2f}')
else:
    print('Emprestimo não aprovado.')
