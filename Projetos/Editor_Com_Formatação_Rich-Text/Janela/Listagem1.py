"""
Width – Largura do widget;
Height – Altura do widget;
Text – Texto a ser exibido no widget;
Font – Família da fonte do texto;
Fg – Cor do texto do widget;
Bg – Cor de fundo do widget;
Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).


Para receber dados do usuário vamos usar o widget 'Entry'
"""

import tkinter as tk
from tkinter import *
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master) 
        self.widget1.pack()
        # Titulo
        self.msg = Label(self.widget1, text='Primeiro widget')
        self.msg["font"] = ("Calibre", "9", "italic")
        self.msg.pack()
        # Botão
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack()
                

    def mudarTexto(self, event):
        if self.msg["text"] == 'Primeiro widget':
            self.msg["text"] = 'O botão recebeu um clique'
        else:
            self.msg["text"] = 'Primeiro widget'


root = tk.Tk()
Application(root)
root.mainloop()
