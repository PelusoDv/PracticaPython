
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nacimiento = input("Ingrese su fecha de nacimiento: ")
tituloSecundario = True
matricula = int(input("Ingrese monto de la matricula: "))
cuota = matricula + 1000
pythonI = 12000/4
print()
print("====================================================")
print("======= Uiversidad de Python - Inscripciones =======")
print("====================================================")
print()
print("DATOS DE INGRESO:")
print("Nombre completo: " + nombre)
print("Fecha de nacimiento y Edad: " + nacimiento + " (" + edad + ")")
print("Posee título?", tituloSecundario)
print("Matricula:", matricula)
print(f"Cuota Mensual: {cuota}")
print(f"Aransel mensual materia 'Python I': {pythonI}")
print(f"Aransel mensual materia 'Python I' con descuento: {pythonI * 0.85}")