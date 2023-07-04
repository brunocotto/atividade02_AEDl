from Carro import Carro
from Drone import Drone
from PilhaCarro import PilhaCarro
from PilhaDrone import PilhaDrone

pilhaCarros = PilhaCarro()
pilhaDrones = PilhaDrone()

def addCarro():
    marca = str(input("Qual a marca? "))
    modelo = str(input("Qual o modelo? "))
    qtdPortas = int(input("Qual o quantidade de portas? "))

    carro = Carro(marca, modelo, qtdPortas)

    pilhaCarros.add(carro)

def removeCarro():
    pilhaCarros.remover()

def addDrone():
    marca = str(input("Qual a marca? "))
    modelo = str(input("Qual o modelo? "))
    qtdHelices = int(input("Qual o quantidade de hélices? "))

    drone = Drone(marca, modelo, qtdHelices)

    pilhaDrones.add(drone)

def removeDrone():
    pilhaDrones.remover()

def imprimirPilhaCarros():
    pilhaCarros.imprimir()

def imprimirPilhaDrones():
    pilhaDrones.imprimir()

def menu():
    while True:
        choice = input("""
============================
            MENU
============================
[1] Cadastrar Carro
[2] Remover Carro
[3] Cadastrar Drone
[4] Remover Drone
[5] Imprimir Pilha Carros
[6] Imprimir Pilha Drones
[7] Sair
Escolha: """)

        if choice == "1":
             addCarro()
        if choice == "2":
            removeCarro()
        if choice == "3":
            addDrone()
        if choice == "4":
            removeDrone()
        if choice == "5":
            imprimirPilhaCarros()
        if choice == "6":
            imprimirPilhaDrones()
        if choice == "7":
            exit()
menu()