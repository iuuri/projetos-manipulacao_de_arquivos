import os


frutas = ['banana', 'maça', 'uva', 'morango', 'melancia']
cores = ['azul','vermelho','preto','cinza','laranja']
linguagens = ['python','js','c#','java','html']

#Criar arquivo com todas as frutas 
with open ('frutas.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

#Imprimir todas as linhas do arquivo frutas.txt
with open('frutas.txt', 'r', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

#Adicionar todas as cores no arquivo frutas.txt 
with open('frutas.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for cor in cores:
        arquivo.write(cor + os.linesep)

with open ('linguagens.txt', 'w', newline='', encoding='utf-8') as arquivo:
    for linguagem in linguagens:
        arquivo.write (linguagem + os.linesep)