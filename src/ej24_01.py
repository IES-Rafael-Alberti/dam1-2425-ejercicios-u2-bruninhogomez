"Este es el ejercicio 24"
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def main():
    

    numero = int(input("Introduce un número entero positivo: "))
    
    
    if numero < 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        
        cuenta_atras = ', '.join(str(i) for i in range(numero, -1, -1))
        print(cuenta_atras)


if __name__ == "__main__":
    main()