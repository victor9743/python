# aplicacao de salvar nomes e carrega-los
from pathlib import Path

nome = input("Digite seu nome")
cpf = input("Digite seu cpf")

db = Path("db.txt")

with db.open(mode="a") as arquivo:
    arquivo.write(f"nome: {nome} cpf: {cpf} \n")


print("dados salvos com sucesso")


with db.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()


# Remove os caracteres de nova linha
dados_lidos = [linha.strip() for linha in dados_lidos]

print("Db:", dados_lidos)

