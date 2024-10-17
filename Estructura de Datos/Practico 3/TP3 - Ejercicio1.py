
print()
print("-"*25 + " Detector de Palindromos " + "-"*25)
print()

frase = input("Ingrese una palabra o frase para saber si es un palindoromo: \n")

def convertir(string):
    palabras = (string.split())
    juntar = str()
    for palabra in palabras:
        juntar = juntar + palabra
    return juntar.lower()

def invertir(string):
    palabras = (string.split())
    juntar = str()
    for palabra in palabras[::-1]:
        for char in palabra[::-1]:
            juntar = juntar + char
    return juntar.lower()

if convertir(frase) == invertir(frase):
    print(f'"{frase}" Es un palindromo!')
    print()
else:
    print(f'"{frase}" No es un palindromo!')
    print()