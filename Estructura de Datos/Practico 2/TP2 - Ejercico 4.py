
descuentos = {
    "Pesos": 0.9, 
    "Dólares": 0.95, 
    "Yenes": 0.85, 
    "Guaraníes": 0.80, 
    "Otros": 1.1
}

def selecmoneda(num):
    contador = 0
    for x in descuentos:
        if contador == num:
            return x
        contador += 1

def descuentomoneda(num):
    contador = 0
    for x in descuentos:
        if contador == num:
            return descuentos[x]
        contador += 1

cantidad = int(input("¿Cuantos zapallos desea llevar? "))

print()
print("Segun el tipo de moneda al pagar, se aplica un descuento distinto")
print()
for x in descuentos:
    print(x + ":", end=" "), 
    if descuentos[x] > 1:
        print(f"{int(descuentos[x] * 100 - 100)}% de aumento", end="\n")
    elif descuentos[x] < 1:
        print(f"{abs(int(descuentos[x] * 100 - 100))}% de descuento", end="\n")
print()

moneda = (int(input("¿Con que tipo de moneda desea abonar? (Ingrese el numero correspondiente)\n" + f"[1] {selecmoneda(0)} - [2] {selecmoneda(1)} - [3] {selecmoneda(2)} - [4] {selecmoneda(3)} - [5] {selecmoneda(4)}: "))) - 1

comprador = input("Ingrese su nombre de cliente o empresa\n")

print()
print("="*22 + " RECIBO " + "="*22)
print("="*52)
print()
print("CLIENTE:", comprador)
print("COMPRA: Zapallos por ", cantidad, "unidades a $1000c/u")
print("MONEDA DE PAGO: ", end=""), print(selecmoneda(moneda))
if descuentomoneda(moneda) < 1:
    print(f"DESCUENTO: {abs(int(descuentomoneda(moneda) * 100 - 100))}%")
elif descuentomoneda(moneda) > 1:
    print(f"AUMENTO: {int(descuentomoneda(moneda) * 100 - 100)}%")
print("TOTAL A PAGAR: $", (float(cantidad * 1000)) * descuentomoneda(moneda))