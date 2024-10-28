"Este es el ejercicio 25"
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
#y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


def pedir_cantidad_inversion():
    while True:
        try:
            cantidad = float(input("Introduce la cantidad a invertir: "))
            if cantidad <= 0:
                print("Por favor, introduce una cantidad positiva.")
            else:
                return cantidad
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

def pedir_interes_anual():
    while True:
        try:
            interes = float(input("Introduce el interés anual (en porcentaje, por ejemplo 5 para 5%): "))
            if 0 < interes <= 100:
                return interes / 100  
            else:
                print("El interés debe estar entre 0 y 100. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

def pedir_anios_inversion():
    while True:
        try:
            anios = int(input("Introduce el número de años de la inversión: "))
            if 0 < anios <= 70:
                return anios
            else:
                print("El número de años debe ser positivo y no mayor a 70. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

def main():
    
    cantidad = pedir_cantidad_inversion()
    interes = pedir_interes_anual()
    anios = pedir_anios_inversion()
    
    
    print("\nCapital obtenido cada año:")
    for anio in range(1, anios + 1):
        capital = cantidad * (1 + interes) ** anio
        print(f"Año {anio}: {capital:.2f}")


if __name__ == "__main__":
    main()