"Este es el ejercicio 27"

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()  


def main():
    for numero in range(1, 11):
        print(f"Tabla de multiplicar del {numero}")
        tabla_multiplicar(numero)


if __name__ == "__main__":
    main()
