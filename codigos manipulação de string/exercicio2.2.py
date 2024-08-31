
''' DESAFIO 22
# Crie um programa que leia o nome completo de uma pessoas e
# mostre
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome'''

nomeCompleto=input('Digite o seu nome completo:\n')
# O nome com todas as letras maiúsculas
print(nomeCompleto.upper())
# O nome com todas as letras minúsculas
print(nomeCompleto.lower())
# Quantas letras ao todo (sem considerar espaços)

''' primeiro fiz a contagem dos espaços com count() e depois
verifiquei o tamanho com len() fiz a subtração de um pelo outro'''


contagemEspaco=nomeCompleto.count(' ')
tamanhoTexto=len(nomeCompleto)
print(tamanhoTexto-contagemEspaco)
'''Subistitui os espaços do texto com o comando replace() e depois verifiquei
o tamanho com o len() '''
nomeSemEspaco=nomeCompleto.replace(' ','')
print(len(nomeSemEspaco))
#--------------------------------------------
# Quantas letras tem o primeiro nome
'''Utilizei o comando split() com [] para salvar apenas o primeiro nome e depois
verifiquei o tamanho com o len()'''
primeiroNome=nomeCompleto.split()[0]
print(len(primeiroNome))
#--------------------------------------------
''' find(' ') vali localizar o primeiro espaço que seria uma posição onde termina
'''
print(nomeCompleto.find(' '))