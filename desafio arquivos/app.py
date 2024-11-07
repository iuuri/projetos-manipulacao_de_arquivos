import os

#Exibir todos arquivos que estão na pasta
print(os.listdir())

#Exibir o caminho absoluto dos arquivos 
arquivos = os.listdir()
for arquivo in arquivos:
    print(os.path.join(os.getcwd() + os.sep + arquivo))

#Exibir o caminho absoluto dos arquivos da subpasta 
#mudar diretorio 
os.chdir(os.getcwd() + os.sep + 'desafio arquivos' + os.sep + 'desafio textos')
#Iterar sobre os arquivos 
arquivos = os.listdir()
for arquivo in arquivos:
    print(os.path.join(os.getcwd() + os.sep + arquivo))


#Navegar entres as pastas 
print (os.getcwd())

os.chdir(os.pardir)
print (os.getcwd())

os.chdir(os.pardir)
print (os.getcwd())

