print("=========== AULAS ===========")
dia = int(input("Ingrese el numero de dia del 1 (lunes) al 6 (sábado): "))
if dia % 2 == 0:
    print("Aula: A-300")
else:
    print("Aula: A-315")

print()

print("========= DESCUENTOS =========")
cuota = 10000
turno = input("Ingrese el turno (Mañana, Tarde o Noche): ")
cantMat = int(input("Ingrese la cantidad de materias: "))
if turno.lower() == "tarde" and cantMat >= 3:
    print(f"El valor de la cuota es: {cuota*0.75}")
else:
    print(f"El valor de la cuota es: {cuota*0.95}")

print()

print("====== ESTACIONAMIENTO ======")
vehiculo = input("Ingrese el tipo de vehiculo (Auto, Moto o Bicicleta): ")
if vehiculo.lower() == "bicicleta" or vehiculo.lower() == "bici":
    print("El valor del estacionamiento es: 50")
else:
    print("El valor del estacionamiento es: 300")