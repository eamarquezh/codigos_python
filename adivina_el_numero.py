import random
from typing import Mapping


def run():
    vidas = 3
    numero_aleatorio = random.randint(1,10)
    numero_elegido = 0
    while numero_elegido != numero_aleatorio:
        numero_elegido = int(input("elige un numero del 1 al 10(vidas:" + str(vidas) + "): "))
        if numero_aleatorio > numero_elegido:
            print("deberas elegir un numero mayor")
            vidas -= 1
        elif numero_aleatorio < numero_elegido:
            vidas -= 1
            print("deberas elegir un numero menor")
        elif numero_aleatorio == numero_elegido:
            print("Ganaste :)")
            break
        elif vidas == 0:
            print("Perdiste :(")
            break


if __name__ == '__main__':
    run()
