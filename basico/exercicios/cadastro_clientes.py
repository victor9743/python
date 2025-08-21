def cadastrar_cliente(nome, email, telefone):
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome}, {email}, {telefone} \n")
    print("cliente cadastrado com sucesso !!!")


def listar_cliente():
    try:
        with open("clientes.txt", "r") as arquivo:
            clientes = arquivo.readlines()

            if not clientes:
                print("nenhum cliente encontrado !!!")
            else:
                print("lista de clientes cadastrados")

                for cliente in clientes:
                    nome, email, telefone = cliente.strip().split(",")

                    print(f"Nome: {nome} E-mail: {email} Telefone: {telefone}")
    except FileNotFoundError:
        print("Nenhum Arquivo Encontrado")

def salvar_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for dado in dados:
            arquivo.write(f"{dado} \n")

def ler_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return []

cadastrar_cliente("victor", "teste@teste.com", "34324323432")
cadastrar_cliente("joão", "teste2@teste.com", "343345345332")
listar_cliente()


