
monedaydescuentos = {
    "Pesos": 0.9, 
    "Dólares": 0.95, 
    "Yenes": 0.85, 
    "Guaraníes": 0.80, 
    "Otros": 1.1
}

producto = "Zapallo"
precio = 1000
cliente = input("Ingrese su nombre de cliente o empresa: ")

def selecmoneda(num):
    contador = 0
    for x in monedaydescuentos:
        if contador == num:
            return x
        contador += 1

def recibo(moneda, cantidad):
    descuento = monedaydescuentos[selecmoneda(moneda)]
    print("="*22 + " RECIBO " + "="*22)
    print("="*52)
    print("CLIENTE:", cliente)
    print(f"COMPRA: {producto} por {cantidad} unidades a ${precio}c/u")
    print("MONEDA DE PAGO: ", end=""), print(selecmoneda(moneda))
    if descuento < 1:
        print(f"DESCUENTO: {abs(int(descuento * 100 - 100))}%")
    elif descuento > 1:
        print(f"AUMENTO: {int(descuento * 100 - 100)}%")
    print("TOTAL A PAGAR: $", (float(cantidad * precio)) * descuento)
    print("="*52)

def programa():
    cantidad = int(input(f"¿Cuantos/as {producto} desea llevar? "))
    print()
    print("¿Con que tipo de moneda desea abonar? (Ingrese el numero correspondiente)")
    for x in range(len(monedaydescuentos)):
        print(f"[{x+1}] {selecmoneda(x)}:", end=" "), 
        if monedaydescuentos[selecmoneda(x)] > 1:
            print(f"{int(monedaydescuentos[selecmoneda(x)] * 100 - 100)}% de aumento", end="\n")
        elif monedaydescuentos[selecmoneda(x)] < 1:
            print(f"{abs(int(monedaydescuentos[selecmoneda(x)] * 100 - 100))}% de descuento", end="\n")
    moneda = int(input()) - 1
    print()
    recibo(moneda, cantidad)
    print()

programa()
