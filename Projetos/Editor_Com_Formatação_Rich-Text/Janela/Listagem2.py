from tkinter import *

class Application:
    def __init__(self, master=None):
        # Primeiro
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        # Segundo
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        # Terceiro
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        # Quarto
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        # Titulo
        self.titulo = Label(self.primeiroContainer, text='Dados do usuário')
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text='Nome', font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        # Nome
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        # Senha
        self.senha = Label(self.terceiroContainer, text='Senha', font=self.fontePadrao)
        self.senha.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        # Autenticação
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = 'Autenticar'
        self.autenticar["font"] = ("Calibre", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mesagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mesagem.pack()

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mesagem["text"] = "Autenticado"

        else:
            self.mesagem["text"] = "Erro na autenticação"



root = Tk()
Application(root)
root.mainloop()