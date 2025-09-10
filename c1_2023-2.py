def misterio(obra, s, n):
    i = 0
    j = 0
    while i < len(obra):
        if obra[i] == s:
            j += 1
        if j == n:
            return i
        i += 1
    return -1


def repetir(seccion):
    primer_indice = misterio(seccion, ":", 1)
    segundo_indice = misterio(seccion, ";", 1)

    numero = int(seccion[primer_indice + 1: segundo_indice])

    nuevo_string = seccion[:primer_indice]


    comodin = False

    if "*" in seccion:
        comodin = True
    

    if comodin == True:
        cadena2 = ""

        for caracter in nuevo_string:
            if caracter not in "b#":
                cadena2 += caracter
    
        print(cadena2 * numero)
    else:
        print(nuevo_string * numero)



repetir("CbCBAAB#:3;")
