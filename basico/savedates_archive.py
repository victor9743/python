from pathlib import Path

# define o caminho do arquivo
caminho_do_arquivo = Path("teste.txt")

# dados para salvar no arquivo
dados_para_salvar = ["Python", "C++", "Java"]

# Abre o arquivo no modo escrita e salva os dados
with caminho_do_arquivo.open(mode='w') as arquivo:
    for item in dados_para_salvar:
        arquivo.write(f"{item}\n")

print("Dados Salvos Com Sucesso")

# carregar dados de um arquivo

with caminho_do_arquivo.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()


# Remove os caracteres de nova linha
dados_lidos = [linha.strip() for linha in dados_lidos]

print("Dados lidos do arquivo:", dados_lidos)
