"Este es el ejercicio 28"

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

def dibujar_triangulo(filas):
    for i in range(1, filas + 1):
        print('*' * i)


def main():
    
    numero_filas = int(input("Introduce un número entero para el tamaño del triángulo: "))
    print("Triángulo rectángulo:")
    dibujar_triangulo(numero_filas)


if __name__ == "__main__":
    main()