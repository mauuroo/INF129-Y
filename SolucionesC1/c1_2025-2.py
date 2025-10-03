def validar(pedido):
    p = 0
    for c in pedido:
        if c == "[":
            p += 1
        elif c == "]":
            p -= 1
        elif c not in "HVQTLNCPKMZB":
            return False
        if abs(p) > 1:
            return False
    if p == 0:
        return True
    return False

def costo_pedido(pedido):
    cadena = "" #La cadena que retornaremos al programa
    ingrediente = False #Verifica si me encuentro leyendo ingredientes o no
    contador_sandwich = 0 #Cuenta los sandwiches que hemos analizado
    costo = 100 #Precio base del primer sandiwch
    if validar(pedido): #Validamos el pedido
        for caracter in pedido: #Recorremos cada caracter el string
            if caracter == "[": #Sabemos que la proxima iteracion leeremos un nuevo sandiwch
               ingrediente = True #Leeremos ingredientes para la proxima iteracion
               contador_sandwich += 1 #Aumento el contador de sandwich
            elif caracter == "]": #Termine de leer un sanwidch
                ingrediente = False 
        
            if ingrediente:
                if caracter in "HVP": #Válido también if caracter == "H" or caracter == "P":
                    costo += 1000
                elif caracter in "QB":
                    costo += 700
                elif caracter in "TLCÑ":
                    costo += 500
                elif caracter in "KMZ":
                    costo += 300

            else: #Ingrediente == False (ya sumamos los costos de un sandwich completo)
                cadena += "H" + str(contador_sandwich) + ": " + str(costo) + "; " #Concatenamos a la cadena completa la info de este sandwich

                costo = 100 #Volvemos a declarar costo en 100 pues el proximo sandiwch que se lea debe partir en 100 de base
        return cadena
        

    else:
        return "Error en el pedido"
    
print(costo_pedido("[H][HQ]"))
print(costo_pedido("[HHLTKMB][HQH][HCKMB][H]"))
print(costo_pedido("HDHHALKMB]"))