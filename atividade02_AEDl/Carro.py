from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo = None, marca = None, qtdportas = None):
        super().__init__(modelo, marca)
        self.__qtdportas = qtdportas
        self.proximo = None

    def __str__(self):
        super().imprimir()
        print("Qtd Portas: ", self.__qtdportas)
