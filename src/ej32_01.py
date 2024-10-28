"Este es el ejercicio 32"

#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.



def contar_letra(frase, letra):
    return frase.count(letra)


def main():
    
    frase = input("Introduce una frase: ")
    
    letra = input("Introduce una letra: ")

    
    if len(letra) != 1:
        print("Por favor, introduce solo una letra.")
    else:
        
        cantidad = contar_letra(frase, letra)
        print(f"La letra '{letra}' aparece {cantidad} veces en la frase.")


if __name__ == "__main__":
    main()
