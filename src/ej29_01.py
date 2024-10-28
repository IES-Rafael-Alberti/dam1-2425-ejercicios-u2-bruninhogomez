"Este es el ejercicio 29"

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def verificar_contraseña(contraseña_correcta):
    
    contraseña = input("Introduce la contraseña: ")
    return contraseña == contraseña_correcta

def main():
    
    contraseña_correcta = "contraseña"  
    while not verificar_contraseña(contraseña_correcta):
        print("Contraseña incorrecta. Inténtalo de nuevo.")
    print("¡Contraseña correcta!")


if __name__ == "__main__":
    main()