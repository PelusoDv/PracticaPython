
fecha = []

def cargafecha():
    contador = 0
    print("Ingrese 3 numeros correspondientes a una fecha: ")
    for x in range(3):
        if contador == 0:
            x = fecha.append(int(input("Día: ")))
            while fecha[contador] < 0:
                fecha[contador] = (int(input("Error! ingrese el dia nuevamente: ")))
        elif contador == 1:
            x = fecha.append(int(input("Mes: ")))
            while fecha[contador] < 0:
                fecha[contador] = (int(input("Error! ingrese el mes nuevamente: ")))
        elif contador == 2:
            x = fecha.append(int(input("Año: ")))
            while fecha[contador] < 0:
                fecha[contador] = (int(input("Error! ingrese el año nuevamente: ")))
        contador += 1
        
def verifecha(a,b,c):
    dia = False
    mes = False
    año = True

    if b < 8 and b != 2:
        mes = True
        if b % 2 == 0:
            if a <= 30:
                dia = True
        else:
            if a <= 31:
                dia = True
    if b > 7 and b < 13:
        mes = True
        if b % 2 == 0:
            if a <= 31:
                dia = True
        else:
            if a <= 30:
                dia = True
    if b == 2:
        mes = True
        if c < 100 and c % 4 == 0:
            if a <= 29:
                dia = True
        elif 400 > c > 100 and (c % 4 == 0 and c % 100 == 0):
            if a <= 29:
                dia = True
        elif c > 400 and (c % 4 == 0 and c % 100 == 0 and c % 400 == 0):
            if a <= 29:
                dia = True
        else:
            if a <=28:
                dia = True

    if dia and mes and año:
        print(True)
    else:
        print(False)
    
cargafecha()
verifecha(fecha[0],fecha[1],fecha[2])