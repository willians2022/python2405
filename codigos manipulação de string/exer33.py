num1=int(input('Digite um numero'))
num2=int(input('Digite um numero'))
num3=int(input('Digite um numero'))

#  se num1 maior que num2 e num1 maior que num3
if num1 > num2 and num1 > num3:
        maior=num1
#  se num2 maior que num1 e num2 maior que num3
if num2 > num1 and num2 > num3:
        maior=num2
#  se num3 menor que num2 e num3 menor que num1
if num3 > num2 and num3 > num1:
        maior=num3
#  se num1 menor que num2 e num1 menor que num3
if num1 < num2 and num1 < num3:
        menor=num1
#  se num2 menor que num1 e num2 menor que num3
if num2 < num1 and num2 < num3:
        menor=num2
#  se num3 maior que num2 e num3 maior que num1
if num3 < num2 and num3 < num1:
        menor=num3
print(f'O maior numero é o {maior}\nO menor numero é o {menor}')
num1=int(input('Digite um numero'))
num2=int(input('Digite um numero'))
num3=int(input('Digite um numero'))
print(f'O maior numero é o {max(num1,num2,num3)}'
      f'\nO menor numero é o {min(num1,num2,num3)}')