from abc import ABC

class Veiculo(ABC):
    def __init__(self, marca = None, modelo = None):
        self.modelo = modelo
        self.marca = marca

    def imprimir(self):
        print("Modelo", self.modelo)
        print("Marca", self.marca)
