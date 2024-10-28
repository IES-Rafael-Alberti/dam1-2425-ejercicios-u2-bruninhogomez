"Este es el ejercicio 22"
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
#e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculadef verificar_contraseña():


def verificar_contraseña(contrasenia_usuario: str) -> bool:

    if contraseña_usuario.lower() == contraseña.lower():
        return True
    else:
        return False

def main():
    verificar_contraseña()
   
if __name__ == "__main__":
    main()