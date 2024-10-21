"Escribe un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde 1 hasta su edad)"

def pedir_edad()->int:
    edad_correcta = False
    while not edad_correcta:
        try:
            edad = None
            edad = int(input("Introduce tu edad: "))
            if edad < 1:
                raise ValueError("La edad debe ser un numero positivo.")
            if edad == 0:
                raise ValueError("L edad debe ser un numero positivo mayor que cero.")
            if edad > 125:
                raise ValueError("La edad debe ser numero menor o igual a 125.")
            edad_correcta = True
        except ValueError as e:
            if  edad is None:
                print(f"ERROR* El nùmero introducido no es un número entero válido. Inténtelo de nuevo.")
            else:
                print(f"ERROR* {e}. Inténtelo de nuevo.")
    return edad
            

def mostrar_anios_cumplidos(edad:int):
    for i in range(1 , edad + 1):
        if i == edad:
            print(i)
        else:
            print(i, end=", ")
    

def main():
    edad = pedir_edad()
    print (f"Has cumplido los siguientes años:")
    mostrar_anios_cumplidos(edad)


if __name__=="__main__":
    main()