#Necesito un contador
#necesito hacerlo con un while
#Necesito una cadena de texto, para lo que tengo retornar
#Necesito la longitud de la cadena, para calcular el N


def obtener_columna(imagen, columna):
    i = 0
    n = int(len(imagen) ** 0.5)
    cadena_nueva = ""
    numero_fila = 1 #Me dice en que fila voy

    while i < len(imagen):
        fila = misterio(imagen, numero_fila)
        cadena_nueva += fila[columna - 1]

        i += n
        numero_fila += 1


    return cadena_nueva 
