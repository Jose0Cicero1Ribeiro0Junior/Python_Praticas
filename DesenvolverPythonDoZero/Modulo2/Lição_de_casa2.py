"""
Jogos de Monstrinhos são bastante populares
em várias plataformas: consoles, PCs e celulares. Estes monstrinhos são
capturados, alimentados, treinados, evoluem e batalham.

As características da Orientação a Objetos atendem prontamente ao desenvolvimento deste tipo de jogos.



 Herança 
. todos os monstrinhos apresentam recursos comuns: nome , tipo , pontos de saúde , evolução , dados de captura etc; 
. todos os monstrinhos apresentam métodos comuns: alimentar , reviver , desmaiar , evoluir etc; 
. cada tipo específico de monstrinho, fogo, água, terra, pedra, aço, grama, apresenta seus próprios atributos; 
. cada tipo específico de monstrinho apresenta seus métodos próprios.



Encapsulamento 
. Quando ocorre um método de um monstrinho não precisa exatamente o que ocorre internamente na “fisiologia” dele.



Tomando como base o código abaixo: 
a) término de implementar os métodos desmaiar e alimentar da classe TipoMonstro ; 
b) termine de implementar uma classe TipoFogo ; 
c) implemente um método para aumentar a temperatura da TipoFogo e o método incendio que apenas imprime o nome do monstrinho e o texto 'incendio' ; 
d) implemente uma classe TipoAgua com o atributo fluxo e método chuva análogo ao da classe TipoFogo ; 
e) implemente o __str__ para as duas novas classes;
f) crie objetos das classes, use os métodos implementados e imprima os novos atributos.



Capriche, pois iremos sofisticar esse código.
"""
importar datetime como dt



classe TipoMonstro ():

    def __init __ (self, nome, tipo, ps):

        self .nome = nome

        self .tipo = tipo

        self .ps = ps



        self .evolucao = 1

        self .ativo = True

        self .alimentos = 0

        self .data_cap = dt.datetime.today ()



    def __str __ (self):

        s = ''

        s + = 'Nome:% s \ n' % self .nome

        s + = 'Tipo:% s \ n' % self .tipo

        s + = 'Ponto Saude:% d \ n' % self .ps

        s + = 'Evolução:% d \ n' % self .evolucao

        s + = 'Ativo:% s \ n' % self .ativo

        s + = 'Alimentos:% d \ n' % self .alimentos

        s + = 'Captura de dados:% s \ n' % \

            self .data_cap.strftime ( '% d /% m /% Y' )

        return s



    def reviver (self):

        self .ativo = True



    def desmaiar (sef):

        # fazer

        passar



    def evoluir (self):

        self .evolucao + = 1



    def alimentar (self):

        # fazer

        passar



classe TipoFogo (TipoMonstro):

    def __init __ (self, nome, tipo, ps, temperatura):

        # fazer

        passar