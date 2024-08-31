# # Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# Para saber se um ano é bissexto existe uma regra básica: os anos bissextos
# são aqueles múltiplos de 4, ou seja, a cada quatro anos temos um ano
# bissexto.
# Por outro lado, esses anos não são múltiplos de 100 (por exemplo,1800,
# 1900, 2100), exceto os múltiplos de 400 (por exemplo, 1600, 2000, 2400).


ano=int(input('Digite o ano: '))

# %4==0 %100!=0 %400==0
if ano%4==0 and (ano%100!=0 or ano%400==0):
        print('O ano é bissexto')
else:
        print('O ano não é bissexto')
