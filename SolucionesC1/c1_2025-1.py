def misterio(s):
    i = 2
    m = int(s[0])
    while i<len(s):
        if int(s[i]) > m:
            m = int(s[i])
        i += 2
    return m

#Pregunta 2 (2 posibles soluciones)
#Solución 1
def filas_secas(invernadero, umbral):
    filas_secas = 0 #Contador con la cantidad de filas secas
    i = 0

    i_inicial = 0 #Indice de donde comienza una fila

    while i < len(invernadero):
        if invernadero[i] == "|":
            if misterio(invernadero[i_inicial: i]) < umbral:
                filas_secas += 1
            i_inicial = i + 1 #Actualizamos el indice inicial a la posición del último "|" leído + 1, para que la posición sea del número continuo al "|"
        
        if i == len(invernadero) - 1: #Estamos en la ultima fila pero recordar que no habrá un "| final"
            if misterio(invernadero[i_inicial:]) < umbral:
                  filas_secas += 1
    
        i += 1 #Recordar siempre actualizar el contador

    return filas_secas


#Solución 2
def filas_secas(invernadero, umbral):
    fila = "" #Subcadena que ira sumando cáracteres hasta el final de la fila
    filas_secas = 0
    i_aux = 1 #Indice auxiliar que nos servirá para comparar si estamos en la última fila (no contiene un "|" al final)

    for caracter in invernadero:
        if caracter == "|": #La subcadena s ya contiene una fila
            if misterio(fila) < umbral:
                filas_secas += 1
            fila = "" #Como ya analizamos una fila, hay que resetear a "" el valor de la subcadena
        else:
            fila += caracter #Sumamos cáracteres
        
        if i_aux == len(invernadero): #Estamos en la última fila ya que el indice auxiliar es igual al largo de la cadena completa
            if misterio(fila) < umbral:
                filas_secas += 1

        i_aux += 1

    return filas_secas




#PREGUNTA 3
#Código principal
umbral = int(input("Ingrese valor umbral: "))
flag = True
h_promedio_max = 0
h_promedio_min = 10000000000000 #Un valor muy alto para que se pueda actualizar al comparar

while flag: #RECORDAR ACTUALIZAR ESTA VARIABLE DENTRO DEL BUCLE!
    invernadero = input("Ingrese estado de un invernadero: ")
    filas_s = filas_secas(invernadero, umbral) #¡PORFAVOR RECUERDEN NO LLAMAR A UNA VARIABLE CON EL MISMO NOMBRE QUE USA UNA FUNCIÓN!

    print("Secas:", filas_s) #Recordar que al usar , ya hay un " " (espacio en blanco)
    
    if filas_s == 0:
        flag = False #El bucle termina
    else:
        humedad = 0
        n_secciones = 0 #Número de secciones, útil para calcular el promedio

        for caracter in invernadero:
            if caracter != "|" and caracter != "-": #Como les mencione en clase, también es valido: if caracter not in "|-"
                humedad += int(caracter)
                n_secciones += 1

        promedio = round(humedad / n_secciones)
        print("Humedad promedio:", promedio) 

        if promedio > h_promedio_max:
            h_promedio_max = promedio
        
        if promedio < h_promedio_min:
            h_promedio_min = promedio

print("Humedad promedio máxima:", h_promedio_max)
print("Humedad promedio mínima:", h_promedio_min)
