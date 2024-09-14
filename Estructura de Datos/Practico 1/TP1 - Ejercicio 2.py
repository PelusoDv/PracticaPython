
nota1 = int(input("Ingrese la nota del primer parcial: "))
nota2 = int(input("Ingrese la nota del segundo parcial: "))
promedio = (nota1 + nota2) / 2
msj = "Progreso del 1er al 2do parcial: "

print()
print("El promedio de las notas es:", promedio)

if nota2 >= 7:
    print("Aprobó el segundo parcial")
else:
    print("Desaprobó el segundo parcial")

if nota2 > nota1:
    print(msj + "Mejoró su desempeño")
elif nota2 == nota1:
    print(msj + "Mantuvo la nota")
else:
    print(msj + "Empeoró su desempeño")

if promedio >= 7:
    print("Promocionado")
elif promedio >=4:
    print("Debe rendir final")
else:
    print("Debe recursar")