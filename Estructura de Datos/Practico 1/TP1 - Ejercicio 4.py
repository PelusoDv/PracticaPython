
linelenght = 15
daylenght = 6
arglenght = 30

print()
print("="*linelenght + " Listado de aulas " + "="*linelenght)
dias = [1,2,3,4,5,6]
print(" "*daylenght + "Dia" + " "*arglenght + "Aula")
for x in dias:
    if x % 2 == 0:
        print(" "*daylenght ,x, end = " "), print(" "*(arglenght-1) + "A- 300", end = "\n")
    else:
        print(" "*daylenght ,x, end = " "), print(" "*(arglenght-1) + "A- 315", end = "\n")

print()
print("="*(linelenght+1) + " Carga de edades " + "="*(linelenght+1))
contador = 0
edad = int(input("Ingrese una edad mayor o igual a 18: "))
while edad < 18:
    edad = int(input("Error! La edad debe ser mayor o igual a 18: "))
    contador += 1
print("La edad ingresada es: ", edad)
print("Se ingreso la edad erroneamente ", contador, " veces")

print()
print("="*linelenght + " Promedio de notas " + "="*linelenght)
notas = 0
for x in range(5):
    notas = notas + int(input("Ingrese la nota: "))
print("El promedio de notas es: ", notas/5)

print()
print("="*linelenght + " Costo del comedor " + "="*linelenght)
costo = 1250
print(" "*daylenght + "Dia" + " "*arglenght + "Costo")
for x in range(6):
    print(" "*daylenght ,x + 1 , end = " "), print(" "*(arglenght-1) + "$", costo*(x + 1), end = "\n")