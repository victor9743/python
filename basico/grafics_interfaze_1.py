import tkinter as tk

class Acao:
    contador = 0

    @classmethod
    def incrementar(cls):
        texto = entrada.get()
        cls.contador += 1
        rotulo.config(text=texto)




# criar a janela principal
janela = tk.Tk()
janela.title('Minha primeira janela')
janela.geometry('500x500')


# criar um rotulo
rotulo = tk.Label(janela, text=f'contador: {Acao.contador}')
rotulo.pack()

entrada = tk.Entry(janela)
entrada.pack()

# criando um botão
botao = tk.Button(janela, text='Aumentar', command=Acao.incrementar)
botao.pack()

# Executar a aplicação
janela.mainloop()

