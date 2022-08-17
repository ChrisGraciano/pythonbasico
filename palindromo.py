def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Por favor, Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("La palabra indicada SI ES UN PALÌNDROMO")
    else:
        print("La palabra indicada NO ES UN PALÌNDROMO")
    

if __name__ == "__main__":
    run()