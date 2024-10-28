"Este es el ejercicio 26"

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.


def pedir_altura():
    while True:
        try:
            altura = int(input("Introduce la altura del triángulo (número entero positivo): "))
            if altura > 0:
                return altura
            else:
                print("Por favor, introduce un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

def construir_triangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)

def main():
    
    altura = pedir_altura()
    
    
    construir_triangulo(altura)


if __name__ == "__main__":
    main()