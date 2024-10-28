"Este es el ejercicio 30"

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def es_primo(numero):
    """Función que verifica si un número es primo."""
    if numero <= 1:
        return False  
    for i in range(2, int(numero**0.5) + 1):  
        if numero % i == 0:
            return False  
    return True  

def main():
    try:
        numero = int(input("Introduce un número entero: "))
        if es_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")


if __name__ == "__main__":
    main()
