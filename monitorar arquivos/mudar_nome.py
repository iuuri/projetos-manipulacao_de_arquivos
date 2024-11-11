from watchfiles import watch
import os

# Diretório a ser monitorado
diretorio = os.getcwd()

NEW_FILE = 1
MODIFIED = 2
DELETED = 3

# Variáveis para o novo nome e a extensão do arquivo
nome = 'novo'
extensao = '.pdf'  # Inclua o ponto para a extensão

# Função para gerar o novo nome do arquivo
def novo_nome(arquivo_antigo):
    # Define o novo nome usando as variáveis
    novo_nome = f"{nome}{extensao}"
    # Retorna o novo caminho completo no diretório de monitoramento
    return os.path.join(diretorio, novo_nome)

for mudanca in watch(diretorio):
    for operacao in mudanca:
        tipo_operacao = operacao[0]
        arquivo = operacao[1]

        if tipo_operacao == NEW_FILE:
            # Verifica se o arquivo já foi renomeado para evitar loops
            if nome not in arquivo:
                print(f'Arquivo criado: {arquivo}')
                try:
                    # Gera o novo caminho completo
                    novo_caminho = novo_nome(arquivo)
                    os.rename(arquivo, novo_caminho)
                    print(f'Arquivo renomeado para: {novo_caminho}')
                except Exception as e:
                    print(f"Erro ao renomear: {e}")
        
        elif tipo_operacao == MODIFIED:
            print(f'Arquivo modificado: {arquivo}')
        
        elif tipo_operacao == DELETED:
            print(f'Arquivo excluído: {arquivo}')
