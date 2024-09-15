
fecha = []

def cargafecha():
    for x in range(3):
        if x == 0:
            fecha.append(int(input("Ingrese un Día: ")))
            while fecha[x] < 0:
                fecha[x] = (int(input("Error! ingrese el dia nuevamente: ")))
        elif x == 1:
            fecha.append(int(input("Ingrese un Mes: ")))
            while fecha[x] < 0:
                fecha[x] = (int(input("Error! ingrese el mes nuevamente: ")))
        elif x == 2:
            fecha.append(int(input("Ingrese un Año: ")))
            while fecha[x] < 0:
                fecha[x] = (int(input("Error! ingrese el año nuevamente: ")))
        
def verifecha(a,b,c):
    dia = False
    mes = False

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
        if c <= 100 and c % 4 == 0:
            if a <= 29:
                dia = True
        elif 400 >= c > 100 and (c % 4 == 0 and c % 100 == 0):
            if a <= 29:
                dia = True
        elif c > 400 and (c % 4 == 0 and c % 100 == 0 and c % 400 == 0):
            if a <= 29:
                dia = True
        else:
            if a <=28:
                dia = True

    if dia and mes:
        print("La fecha es valida")
    else:
        print("La fecha no es valida")
    
cargafecha()
verifecha(fecha[0],fecha[1],fecha[2])