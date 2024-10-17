
cadena = "((((((((()))))))))"

def equilibrio_corchete(cad):
    abiertos = int()
    cerrados = int()
    equilibrio = bool()
    for char in cad:
        if char == "(":
            abiertos += 1
        elif char == ")":
            cerrados += 1
    if abiertos == cerrados:
        equilibrio = True
    else:
        equilibrio = False
    return equilibrio

def comparar_corchete(cad):
    char_act = str()
    char_ant = str()
    balanc = True
    for char in cad:
        char_ant = char_act
        char_act = char
        if char_act == "(" and char_ant == ")":
            balanc = False
    return balanc


if equilibrio_corchete(cadena) and comparar_corchete(cadena):
    print("Condicion 1: " + str(equilibrio_corchete(cadena)))
    print("Condicion 2: " + str(comparar_corchete(cadena)))
    print("La cadena de corhcetes esta balanceada")
else:
    print("Condicion 1: " + str(equilibrio_corchete(cadena)))
    print("Condicion 2: " + str(comparar_corchete(cadena)))
    print("la cadena de corchetes no esta balanceada")