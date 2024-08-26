texto = "curso de python "
#imprimir a variavel
print(texto)

#imprimindo texto por posição
print(texto[-1])

# mostra a ultima letra do texto nesse caso o espaço
print(texto[-2])

#mostra a penultima letra do texto nesse caso o "n"
print(texto[9:15])

#apartir da 10 posição  até a posição 16, pulando de dois em dois
print(texto[9:15:2])

#do  inicio até a 9 posição
print(texto[:8])

#da 9 posição até a ultima
print(texto[8:])

#mostra o tamanho do texto com espaços
print(len(texto))

#(count) conta quantas vezes aparece a palavra 
print(texto.count('python'))

#(find) verifica se tem na frase e mostre a sua primeira  posição 
print(texto.find('python'))

#(in) verifica se tem nba frase e retorna true ou false 
print("python" in texto)

#(replace) substuir a palavra antiga pela nova 
print(texto.replace("python","java"))

#(upper) todas as letras maiuscula 
print(texto.upper())

#(lower) todas as letras minuscula
print(texto.lower())

#(capitalizer) apenas a primeira letra maiuscula
print(texto.capitalize())

#(title) colocar todas letra iniciais das palavras maiuscula
print(texto.title())

#(strip) remova os espaços inuteis
print(texto.strip())

#(rstrip) remova os espaço inuteis da direita 
print(texto.rstrip())

#(lstrip) remova o espaço inuteis da esquerda 
print(texto.lstrip())

#"+" (join) adiciona o caracter no meio de cada caracter 
print("+".join(texto))

#(split) adicionar um array no meio de cada caracter como  forsse um lista  
print(texto.split())

#(fraseDividida) em um array e mostra a ultima palavra
fraseDividida=texto.split()
print(fraseDividida[-1])

#(rfind) encontra a ultima palavra 
texto= "curso de python "
print(texto.rfind("curso"))

