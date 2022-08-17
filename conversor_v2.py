def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
💵 Bienvenido Al Conversor de Monedas Latinas de Chris 💵

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una de las anteriores opciones: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 4426)
elif opcion == 2:
    conversor("Argentinos", 131)
elif opcion == 3:
    conversor ("Mexicanos", 20)
else:
    print("Por favor ingresa una opción valida")


