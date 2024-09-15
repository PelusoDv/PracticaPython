
cantidad = int(input("¿Cuantos zapallos desea llevar? "))
print()
print("Segun el tipo de moneda al pagar, se aplica un descuento distinto")
print()
descuentos = {"Pesos": 0.9, "Dólares": 0.95, "Yenes": 0.85, "Guaraníes": 0.80, "Otros": 1.1}
for x in descuentos:
    print(x + ":", end=" "), 
    if descuentos[x] > 1:
        print(f"{int(descuentos[x] * 100 - 100)}% de aumento", end="\n")
    elif descuentos[x] < 1:
        print(f"{abs(int(descuentos[x] * 100 - 100))}% de descuento", end="\n")
print()
moneda = int(input("¿Con que tipo de moneda desea abonar? (Ingrese el numero correspondiente)\n" + "[1] Pesos - [2] Dolares - [3] Yenes - [4] Guaranies - [5] Otro: "))
comprador = input("Ingrese su nombre de cliente o empresa\n")

def descuentomoneda(num):
    contador = 1
    for x in descuentos:
        if contador == num:
            return descuentos[x]
        contador += 1

pagar = (float(cantidad * 1000)) * descuentomoneda(moneda)

def selecmoneda(num):
    contador = 1
    for x in descuentos:
        if contador == num:
            print(x)
        contador += 1

print()
print("="*52)
print("="*22 + " RECIBO " + "="*22)
print("="*52)
print()
print("CLIENTE:", comprador)
print("COMPRA: Zapallos por ", cantidad, "unidades a $1000c/u")
print("MONEDA DE PAGO: ", end=""), selecmoneda(moneda)
if descuentomoneda(moneda) < 1:
    print(f"DESCUENTO: {abs(int(descuentomoneda(moneda) * 100 - 100))}%")
elif descuentomoneda(moneda) > 1:
    print(f"AUMENTO: {int(descuentomoneda(moneda) * 100 - 100)}%")
print("TOTAL A PAGAR: $", pagar)