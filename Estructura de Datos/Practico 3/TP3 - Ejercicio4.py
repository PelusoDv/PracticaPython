
espacio = 25
abcd = ["A-", "B-", "C-", "D-", "E-", "F-", "G-"]
filas_asientos = list()
datos_reserva = list()

def datos_inicial():
    for i in range(7):
        datos = dict()
        for x in range(10):
            datos[str(x + 1)] = str(x + 1)
        datos_reserva.insert(i, datos)

def salon_inicial():
    for i in range(7):
        asientos = dict()
        for x in range(10):
            asientos[abcd[i] + str(x + 1)] = True
        filas_asientos.insert(i, asientos)

def menu():
    menu = ["Ver asientos disponibles", "Reservar asiento", "Consultar reservas", "Salir"]
    print("Que accion desea realizar?")
    for x in range(len(menu)-1):
        print(f"[{x+1}] {menu[x]}", end=" ")
    print(f"[0] {menu[len(menu)-1]}")
    comando = int(input(" "*5))
    return comando

def consulta_salon():
    print("=" * espacio + " Asientos disponibles " + "=" * espacio)
    print(" " *(espacio + 6) + "- sala 1 -")
    filas_salon()

def filas_salon():
    for x in range(14):
        if (x % 2) == 0:
            print(" " * (espacio//2+4) +  " ".join(filas_asientos[x//2].keys()))    # ID asientos
        elif (x % 2) == 1:
            print(" " * (espacio//2+4) + asientos_disp(x//2))   # Disponibilidad asientos
    print()

def asientos_disp(num):
    columna = list()
    cond = list(filas_asientos[num].values())
    asientodisp = "[O]"
    asientoocup = "[X]"
    for x in range(10):
        if cond[x]:
            columna.append(asientodisp)
        elif not cond[x]:
            columna.append(asientoocup)
    return "_".join(columna)

def registro_datos():
    nombre = input("Ingrese su nombre completo: ")
    telefono = str()
    intento = 0
    while type(telefono) != int:
        try:
            if intento > 0:
                telefono = int(input("Ingrese el nº nuevamente: "))
                while telefono < 1000000000:
                    telefono = int(input("Error! el nº debe tener al menos 10 digitos \n" + "Ingrese el nº nuevamente: "))
            else:
                telefono = int(input("Ingrese su nº de telefono: ")) 
                while telefono < 1000000000:
                    telefono = int(input("Error! el nº debe tener al menos 10 digitos \n" + "Ingrese el nº nuevamente: "))
        except ValueError:
            print("Error! el dato debe ser numerico")
            telefono = str()
            intento += 1
    editar_reserva(nombre, telefono)

def editar_reserva(nombre, telefono):
    contador = 0
    print("Que asiento desea reservar? ", end="")
    for x in select_reserva():
        if contador == 0:
            fila = x
        elif contador == 1:
            asiento = str(x)
        elif contador == 2:
            codigo = x
        contador += 1
    filas_asientos[fila][codigo] = False
    datos_reserva[fila] = {nombre if key == asiento else key: value for key, value in datos_reserva[fila].items()}
    datos_reserva[fila][nombre] = telefono

def consulta_reserva():
    contador = 0
    print("Que asiento desea consultar? ", end="")
    for x in select_reserva():
        if contador == 0:
            fila = x
        elif contador == 1:
            asiento = x
        contador += 1
    cond = list(filas_asientos[fila].values())
    disponible = cond[asiento - 1]
    if disponible:
        print("Asiento disponible")
    elif not disponible:
        print(f"Nombre: {select_nombre(fila, asiento)} - Teléfono: {datos_reserva[fila][select_nombre(fila, asiento)]}")

def select_reserva():
    asiento = input("(Escriba el formato de fila-columna, ej: B-4) \n     ")
    while len(asiento) > 3 or asiento[1] != "-":
        asiento = input("Error! Ingrese el formato correcto: ")
    nºfila = abcd.index(asiento[:2].upper())
    nºasiento = asiento[2]
    return int(nºfila), int(nºasiento), asiento.upper()

def select_nombre(nºfila, nºasiento):
    contador = 0
    for x in datos_reserva[nºfila]:
        if contador == int(nºasiento) - 1:
            return x
        contador += 1
  
salon_inicial()
datos_inicial()
comando = str()
while type(comando) != int:
    try:
        comando = menu()
        while comando != 0:
            if comando == 1:
                consulta_salon()
                print("="*(espacio*3))
                comando = menu()
            elif comando == 2:
                registro_datos()
                print("="*(espacio*3))
                comando = menu()
            elif comando == 3:
                consulta_reserva()
                print("="*(espacio*3))
                comando = menu()
            else:
                print("Ingrese un numero valido!")
                print("="*(espacio*3))
                comando = menu()
    except ValueError:
        print("Error! Debe ingresar un numero")
        comando = str()
        