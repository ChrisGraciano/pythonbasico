import random


def run():
    numero_aleatorio = random.randint(1, 100) #la  funcion randint permite que la computadora seleccione un número aleatorio entre 1 y 100. Para invocar la funcionalidad de numero aleatorio luego de random se debe poner un punto (.)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Por favor piensa en un número más grande")
        else:
            print("Por favor piensa en un número más pequeño")
        numero_elegido = int(input("Por favor elige otro número "))
    print("Felicitaciones has ganado adivinando el número que la computadora estaba pensando")


if __name__ == "__main__":
    run()