# DESAFIO 44
# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
# Á vista dinheiro: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço Normal
# 3x ou mais no cartão: 20% de juros


valorProd=float(input('Digite o valor do produto: '))
menu=input('[1] - Dinheiro\n[2] - cartão á vista\n'
           '[3] - cartão em 2x\n [4] - cartão 3x ou mais')
match menu:
    case '1':
        print(f'O valor do produto é de R${valorProd-(valorProd*0.1):,.2f}')
    case '2':
        print(f'O valor do produto é de R${valorProd - (valorProd * 0.05):,.2f}')
    case '3':
        print(f'O valor do produto é de R${valorProd:,.2f}')
    case '4':
        print(f'O valor do produto é de R${valorProd + (valorProd * 0.2):,.2f}')