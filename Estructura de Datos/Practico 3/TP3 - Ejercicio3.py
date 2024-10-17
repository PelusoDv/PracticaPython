
listaclientes = {
    38188976: "Pedro Perez", 
    25503922: "Roberto Carlos", 
    33016244: "Lionel Messi", 
    36407812: "Nicolás Dávalos", 
    18534222: "Rosa Lilia"
}

def clientes_restantes():
    i = 0
    for x in listaclientes:
        i += 1
    return i
    
def nuevo_cliente():
    nombre = input("Ingrese su nombre completo: ")
    DNI = input("Ingrese su Nº de DNI: ")
    listaclientes[DNI] = nombre
    print(f"Uds es el cliente nº{clientes_restantes()} en espera")

def atender_cliente():
    i = 0
    for x in listaclientes:
        if i == 0:
            print(listaclientes[x])
            cliente = x
            i += 1
    listaclientes.pop(cliente)

def menu():
    menu = ["Registrar cliente", "Consultar cola", "Atender cliente", "Salir"]
    print("Eliga la accion a realizar:")
    for x in range(len(menu)-1):
        print(f"[{x+1}] {menu[x]}", end=" ")
    print(f"[0] {menu[len(menu)-1]}")
    comando = int(input(" "*5))
    return comando

comando = menu()
while comando != 0:
    if comando == 1:
        nuevo_cliente()
        print("="*75)
        comando = menu()
    elif comando == 2:
        print(f"Quedan {clientes_restantes()} clientes por ser atendidos.")
        print("="*75)
        comando = menu()
    elif comando == 3:
        if listaclientes == {}:
            print("Ya no quedan clientes por atender")
            print("="*75)
            comando = menu()
        else:
            print("Siguiente cliente: ", end=""), atender_cliente()
            print("="*75)
            comando = menu()
    else:
        print("Ingrese un numero valido!")
        print("="*75)
        comando = menu()