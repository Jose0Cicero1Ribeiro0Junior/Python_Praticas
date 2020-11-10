# Importando módulo do SQlite
from sqlite3 import connect

class Banco():
    
    def __init__(self):
        self.conexao = connect('banco.db')
        self.createTable()
        
    def createTable(self):
        c = self.conexao.cursor()
        
        c.execute()
        
        self.conexao.commit()
        c.close()
        
        