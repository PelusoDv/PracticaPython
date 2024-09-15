
compra = int(input("Ingrese el monto total de la compra: "))
while compra <= 0:
    compra = int(input("Error! el monto no puede ser menor a '0' \n" + "Ingrese el monto nuevamente: "))

pago = int(input("Ingrese el total del dinero abonado: "))
while pago < compra:
    pago = int(input("Error! el pago no puede ser menor a la compra \n" + "Ingrese el monto nuevamente: "))

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
        
vuelto = pago - compra
contbilletes(vuelto)