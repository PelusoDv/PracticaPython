
<<<<<<< HEAD
def monto_compra():
    compra = str()
    intento = 0
    while type(compra) != int:
        try:
            if intento > 0:
                compra = int(input("Ingrese el total de la compra nuevamente: "))
                while compra <= 0:
                    compra = int(input('Error! el monto no puede ser menor a "0" \n' + "Ingrese el monto nuevamente: "))
            else:
                compra = int(input("Ingrese el monto total de la compra: "))
                while compra <= 0:
                    compra = int(input('Error! el monto no puede ser menor a "0" \n' + "Ingrese el monto nuevamente: "))
        except ValueError:
            print("Error! debe ingresar un numero entero")
            compra = str()
            intento += 1  
    return compra

compra = monto_compra()

def total_pago():
    pago = str() 
    intento = 0    
    while type(pago) != int:
        try:
            if intento > 0:
                pago = int(input("Ingrese el monto abonado nuevamente: "))
                while pago < compra:
                    pago = int(input("Error! el pago no puede ser menor a la compra \n" + "Ingrese el monto nuevamente: "))
            else:
                pago = int(input("Ingrese el total del dinero abonado: "))
                while pago < compra:
                    pago = int(input("Error! el pago no puede ser menor a la compra \n" + "Ingrese el monto nuevamente: "))
        except ValueError:
            print("Error! debe ingresar un numero entero")
            pago = str()
            intento += 1
    return pago

pago = total_pago()
=======
def vuelto():
    first = True
    while True:
        try:
            if first:
                compra = int(input("Ingrese el monto total de la compra: "))
                while compra <= 0:
                    compra = int(input("Error! el monto no puede ser menor a '0' \n" + "Ingrese el monto nuevamente: "))
            else:
                compra = int(input("Ingrese el monto de la compra nuevamente: "))
                while compra <= 0:
                    compra = int(input("Error! el monto no puede ser menor a '0' \n" + "Ingrese el monto nuevamente: "))
            break
        except ValueError:
            print("Error! El valor debe ser numerico")
            first = False

    first = True
    while True:
        try:
            if first:
                pago = int(input("Ingrese el total del dinero abonado: "))
                while pago < compra:
                    pago = int(input("Error! el pago no puede ser menor a la compra \n" + "Ingrese el monto nuevamente: "))
            else:
                pago = int(input("Ingrese el total del dinero nuevamente: "))
                while pago < compra:
                    pago = int(input("Error! el pago no puede ser menor a la compra \n" + "Ingrese el monto nuevamente: "))
            break
        except ValueError:
            print("Error! El valor debe ser numerico")
            first = False
    
    return pago - compra
>>>>>>> 2284d6e5c3f3979a25bcb0572261c61ee616dbfc

def contbilletes(a):
    billetes = [500,100,50,20,10,5,1]
    cantbilletes = []
    if a == 0:
        print("No es necesario dar vuelto")
    else:
        print("El vuelto es de:", a)
        for x in billetes:
            index = (len(cantbilletes))
            cantbilletes.append(int(a / x))
            a -= cantbilletes[index] * x
            if cantbilletes[index] > 0:
                print(f"{cantbilletes[index]} billetes de ${x}")

contbilletes(vuelto())