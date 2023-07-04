from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, modelo = None, marca = None, qtdhelices = None):
        super().__init__(modelo, marca)
        self._qtdhelices = qtdhelices
        self.proximo = None
    
    def __str__(self):
        super().imprimir()
        print("Qtd Hélices: ", self._qtdhelices)