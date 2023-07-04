class PilhaCarro:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, carro):
        if self.topo == None:
            self.topo = carro
        else:
            carro.proximo = self.topo
            self.topo = carro
        self.tamanho += 1
        print("Carro cadastrado com sucesso.")
    
    def imprimir(self):
        print("-----------")
        if self.topo == None:
            print("Pilha Vazia")
        else:
            qtdCarros = 1
            aux = self.topo
            while( aux ):
                print("Carro {}".format(qtdCarros))
                print( aux.__str__() )
                qtdCarros += 1 
                aux = aux.proximo
                print("-----------") 

    def remover(self):
        if self.topo == None:
            print("Pilha Vazia")
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1
            self.imprimir()