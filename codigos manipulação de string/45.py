# DESAFIO 45
# Crie um programa que faça o computador jogar Jokenpô com você:
from random import choice
pc=choice(['tesoura','papel', 'pedra']).title()
jogador=input('Jo-ken-pô\n\npedra\n'
              'tesoura\npapel\n\nEscolha: '.upper())

if jogador.title()==pc:
    print(f'Empate!! ambos escolheram {jogador}')
elif jogador=='tesoura':
    if pc == 'Papel':
        print(f'Jogador venceu\nJogador {jogador} x {pc} PC')
    else:
        print(f'Jogador perdeu\nJogador {jogador} x {pc} PC')
elif jogador.lower()=='papel':
    if pc == 'Pedra':
        print(f'Jogador venceu\nJogador {jogador} x {pc} PC')
    else:
        print(f'Jogador perdeu\nJogador {jogador} x {pc} PC')
elif jogador.lower()=='pedra':
    if pc == 'Tesoura':
        print(f'Jogador venceu\nJogador {jogador} x {pc} PC')
    else:
        print(f'Jogador perdeu\nJogador {jogador} x {pc} PC')
else:
    print('Opção invalida!!')
