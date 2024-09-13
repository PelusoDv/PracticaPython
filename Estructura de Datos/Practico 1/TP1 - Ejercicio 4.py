print()
print("======== Listado de aulas ========")
diasYaulas = ({"Dia": 1, "Aula": "A-315"}, {"Dia": 2, "Aula": "A-300"}, {"Dia": 3, "Aula": "A-315"}, {"Dia": 4, "Aula": "A-300"}, {"Dia": 5, "Aula": "A-315"}, {"Dia": 6, "Aula": "A-300"})
print("Dia      Aula")
for x in diasYaulas:
    print(x["Dia"], end = " "), print("       " + x["Aula"], end = "\n")

print()
print("======== Carga de edades ========")
contador = 0
edad = int(input("Ingrese una edad mayor o igual a 18: "))
while edad < 18:
    edad = int(input("Error! La edad debe ser mayor o igual a 18: "))
    contador += 1
print("La edad ingresada es: ", edad)
print("Se ingreso la edad erroneamente ", contador, " veces")

print()
print("======== Promedio de notas ========")
notas = 0
for x in range(5):
    notas = notas + int(input("Ingrese la nota: "))
print("El promedio de notas es: ", notas/5)

print()
print("======== Costo del comedor ========")
costo = 1250
print("Dia      Costo")
for x in range(6):
    print(x + 1 , end = " "), print("       $", costo * (x + 1), end = "\n")