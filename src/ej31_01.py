"Este es el ejercicio 31"

#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.


def mostrar_letras_invertidas(palabra):
    
    for letra in reversed(palabra):
        print(letra)

def main():
    
    palabra = input("Introduce una palabra: ")
    
    mostrar_letras_invertidas(palabra)


if __name__ == "__main__":
    main()
