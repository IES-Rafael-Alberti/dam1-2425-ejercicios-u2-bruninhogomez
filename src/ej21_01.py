"Este es el ejercicio 21"
def pedir_pass() -> str:
    return input("Introduce la contraseña: ").lower()

def comprobar_pass(pass_usuario, pass_secreta)->bool:

    if pass_usuario == pass_secreta:
        return True
    else:
        return False


def main ():
    pass_secreta = "contraseña"

    pass_usuario = pedir_pass()

    if comprobar_pass(pass_usuario , pass_secreta)==True:
        print("Contraseña correcta")
    else:
        print("ERROR* contraseña incorrecta")
        
if __name__=="__main__":
    main()