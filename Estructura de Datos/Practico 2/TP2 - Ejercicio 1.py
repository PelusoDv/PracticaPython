
numeros = []

def carganum():
    contador = 0
    print("Ingrese 3 numeros positivos para saber cual es el mayor: ")
    for x in range(3):
        x = numeros.append(float(input(f"{contador+1}º numero: ")))
        while numeros[contador] < 0:
            numeros[contador] = (float(input(f"Error! ingrese el {contador+1}º numero nuevamente: ")))
        contador += 1

    
def mayorde3(a, b, c):
    errmsg = "No existe un unico numero mayor que los demas"
    if a != b:
        mayor = max(a, b)
        if mayor != c:
            mayor = max(mayor, c)
            print("El numero mayor es: ", mayor)
        else:
            print(errmsg)
    elif a != c:
        mayor = max(a, c)
        if  mayor != b:
            mayor = max(mayor, b)
            print("El numero mayor es: ", mayor)
        else:
            print(errmsg)
    else:
        print(errmsg)

print()   
carganum()
mayorde3(numeros[0],numeros[1],numeros[2])