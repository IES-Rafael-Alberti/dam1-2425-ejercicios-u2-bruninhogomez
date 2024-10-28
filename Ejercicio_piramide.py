import os

def pedir_numero():
    m = True
    while m :
        try:
            n = int(input("Ingrese un numero: "))
            if n < 0:
                raise ValueError("Un numero no puede ser negativo")
            if n > 20:
                raise ValueError("No puede ser mayor que 20")
        except ValueError as e :
            if n  is None:
                print(f"ERROR , no es valido")
            else :
                print(f"ERROR inesperado {(e)}")
    return n
def borrar_consola():
    os.system("clear")





def main():
    borrar_consola()
    n = pedir_numero()
    cadena = []
    for i in reversed (range (20)):
        for j in range (int(n), -1, -1):
            cadena.append (str(j))
        print("+".join (cadena))
    for i in range (0,20,1):
        for j in range (int(n), -1, -1):
            cadena.append (str(j))
        print("+".join (cadena))

        


if __name__=="__main__":
    main()