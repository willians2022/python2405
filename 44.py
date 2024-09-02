# DESAFIO 44
# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
# Á vista dinheiro: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço Normal
# 3x ou mais no cartão: 20% de juros


valor_prod=float(input('digite o valor do produto : '))
menu = input(' [1] - dinheiro\n [2] - cartao á vista\n'
' [3] - cartao em 2x\n [4] - cartao 3x ou mais... \n'
'Digite sua Opção : ')

match menu :
    case '1':
        print(f'o valor do produto é R$: {valor_prod-(valor_prod*0.1):,.2f}')
    case '2':
        print(f'o valor do produto é RS: {valor_prod-(valor_prod*0.05):,.2f}')
    case '3':
        print(f'o valor do produto é R$: {valor_prod:,.2f}) em duas vezes de {valor_prod/2}')
    case '4':
        print(f'o valor do produto ficara em R$: {valor_prod + (valor_prod*0.2):0.2f}')