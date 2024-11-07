import os
# # Como criar um diretório
# os.mkdir('Música 1')

# # Como criar um sub-diretório
# os.makedirs('Música 2' + os.sep + 'rock')

# Verificar se a pasta(diretório) existe 
try:
    if not os.path.isdir('Música'):
        os.mkdir('Música')
    else:
        print('Diretório já foi criado')
except OSError:
    print('Não foi possível criar este diretório,pois já existe')