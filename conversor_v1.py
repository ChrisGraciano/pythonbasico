menu = """
💵 Bienvenido Al Conversor de Monedas Latinas de Chris 💵

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una de las anteriores opciones: """

opcion = int(input(menu))

if opcion == 1:
    pesos_colombianos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos_colombianos = float(pesos_colombianos)
    valor_dolar = 4426
    dolares = pesos_colombianos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos_argentinos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos_argentinos = float(pesos_argentinos)
    valor_dolar = 131
    dolares = pesos_argentinos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos_mexicanos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos_mexicanos = float(pesos_mexicanos)
    valor_dolar = 20
    dolares = pesos_mexicanos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Por favor ingresa una opción valida")


