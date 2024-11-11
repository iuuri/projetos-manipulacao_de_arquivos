'''
Crie 3 pastas diferentes no seu diretório atual(manualmente):
    * Arquivos 2010
    * Documentação
    * Backup
Agora crie 3 arquivos fora destas pastas
    * nomes.txt
    * inscrições.pdf
    * relatórios.xlsx
1) Copie o arquivo nomes.txt para a pasta 'Arquivos 2010' 
2) Mova o arquivo inscrições.pdf para a pasta 'Documentação'
2) Faça uma cópia da pasta 'Arquivos 2010' e tudo que estiver contido nela para a pasta uma nova pasta chamada 'Backup Arquivos 2010'
3) Compacte todo o conteúdo da pasta 'Documentação' no formato zip
4) Mova o arquivo compactado para dentro da pasta 'Backup'
4) Exclua o diretório 'Arquivos 2010' e 'Documentação' e seus conteúdos
5) Compacte o diretório inteiro, para um arquivo chamado 'Backup Arquivos Python.zip'
6) Antes de ir para o próximo vídeo e ver a solução poste a solução que você criou no link que vou deixar abaixo deste vídeo
'''


# import shutil
# import os

# #Copie o arquivo nomes.txt para a pasta 'Arquivos 2010' 
# arquivo_txt = os.getcwd() + os.sep + 'nomes.txt'
# pasta_arquivos = os.getcwd() + os.sep + 'Arquivos_2010'
# shutil.copy(arquivo_txt, pasta_arquivos)

# #Mova o arquivo inscrições.pdf para a pasta 'Documentação'
# arquivo_inscricoes = os.getcwd() + os.sep + 'inscrições.pdf'
# pasta_documentacao = os.getcwd() + os.sep + 'Documentação'
# shutil.move(arquivo_inscricoes,pasta_documentacao)

# #Faça uma cópia da pasta 'Arquivos 2010' e tudo que estiver contido nela para a pasta uma nova pasta chamada 'Backup Arquivos 2010'
# os.makedirs('Backup' + os.sep + 'Backup Arquivos 2010')
# caminho_pasta_arquivo = os.getcwd() + os.sep + 'Arquivos_2010'
# pasta_arquivo_backup = os.getcwd() + os.sep + 'Backup' + os.sep + 'Backup Arquivos 2010'
# shutil.copytree(caminho_pasta_arquivo,pasta_arquivo_backup,dirs_exist_ok=True)

# # Compacte todo o conteúdo da pasta 'Documentação' no formato zip
# documentacao = os.getcwd() + os.sep + 'Documentação'
# shutil.make_archive('zip_tudo','zip',os.getcwd())

# #Mova o arquivo compactado para dentro da pasta 'Backup'
# arquivo_zip = os.getcwd() + os.sep + 'zip_tudo.zip'
# caminho_pasta_backup = os.getcwd() + os.sep + 'Backup'
# shutil.move(arquivo_zip,caminho_pasta_backup)

# #Exclua o diretório 'Arquivos 2010' e 'Documentação' e seus conteúdos
# pasta_arquivo = os.getcwd() + os.sep + 'Arquivos_2010'
# pasta_documentacao = os.getcwd() + os.sep + 'Documentação'
# shutil.rmtree(pasta_arquivo)
# shutil.rmtree(pasta_documentacao)

# # Compacte o diretório inteiro, para um arquivo chamado 'Backup Arquivos Python.zip'
# shutil.make_archive('diretorio_completo','zip',os.getcwd())

