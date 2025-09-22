"""
Cómo siempre, una de las condiciones a considerar para el certamen es el hecho de que ustedes tendrán que hacerlo en papel. Por lo que antes de empezar a programar con ideas desordenadas y organizarlas en el proceso, lo recomendable es que ustedes antes de siquiera escribir código tengan claro que datos necesitan para implementar la función que les solicitan, con esto no me refiero a los argumentos de entrada de la función, sino a lo que ustedes deben extraer mediante distintas tecnicas a la entrada de la función, para luego implementar lo que les solicitan.
"""


#Pregunta 2
"""Para esta pregunta notar que siempre les dejaran el apartado "Nota:" en el cual les mencionan que pueden hacer uso de la función misterio del ruteo para implementar la solución. En todos los certamenes que he revisado se puede usar esta función para simplificar nuestra implementación, pero para llegar a esto primero debemos identificar con exíto que es lo que hace exactamente la función misterio. Para esto, una gúia podria ser:
    1- Analizar lo que recibe la función misterio del ruteo (la entrada)
    2- Analizar lo que retorno en base a lo que recibia la función.
    3- Analizar la salida de pantalla del ruteo
    4- Relacionar los 3 pasos anteriores para ver si somos capaces de inferir de forma primitiva lo que hace la función (-programación declarativa-)
    5- Para comprobar que la conclusión obtenida del paso 4 es correcta, podemos analizar la función como tal y ver si su código efectivamente hace lo que concluimos.

Observación 1: Si luego de unos minutos no logran inferir que hace la función misterio o como implementarla en nuestra función, es posible considerar no usarla para no desperdiciar los valiosos minutos que tenemos.

Observación 2: Generalmente hacer todo el análisis de la pregunta, junto con considerar lo que necesitamos para implementar la solución e inferir lo que hace la función del ruteo es lo que más tiempo toma, una vez aclaradas todas las ideas y tener una idea más o menos clara de como implementarlo, escribir el código es relativamente más "corto"
"""

def misterio(s):
    i = 2
    m = int(s[0])
    while i<len(s):
        if int(s[i]) > m:
            m = int(s[i])
        i += 2
    return m


#Pregunta 2(2 posibles soluciones)
#Solución 1
def filas_secas(invernadero, umbral):
    #Notar que nos aclaran que no es necesario hacer "validaciones".

    #A partir de la observación 1, podemos concluir que la función misterio se encarga de obtener la sección con el mayor valor de humedad de una fila ingresada.
    #Como se nos solicita retornar la cantidad de filas completamente secas, una estrategía es simplemente obtener el mayor valor de humedad de una fila y compararlo con el umbral ingresado y si se encuentra por debajo, sumar 1 a un contador -> Ahí entra la función misterio.
    
    #Sobre identificar que tendriamos que necesitar para implementar nuestra solución se encuentra: identificar cada fila del invernadero.

    filas_secas = 0 #Contador con la cantidad de filas secas

    #Ahora la estrategia es recorrer cada caracter de invernadero, y cuando nos topemos con un "|" o con el ultimo caracter ingresamos a misterio esa subcadena con indices
    i = 0

    #Indices que indicara el inicio de una fila (el final lo determinara el mismo i)
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
    #Notar que nos aclaran que no es necesario hacer "validaciones".

    #A partir de la observación 1, podemos concluir que la función misterio se encarga de obtener la sección con el mayor valor de humedad de una fila ingresada.
    #Como se nos solicita retornar la cantidad de filas completamente secas, una estrategía es simplemente obtener el mayor valor de humedad de una fila y compararlo con el umbral ingresado y si se encuentra por debajo, sumar 1 a un contador -> Ahí entra la función misterio.
    
    #Sobre identificar que tendriamos que necesitar para implementar nuestra solución se encuentra: identificar cada fila del invernadero.
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
"""
En esta pregunta también se suele dejar el apartado "Nota: " en el cual les mencionan que para el desarrollo de esta pregunta pueden hacer uso tanto de la función de la pregunta 2, como de la función misterio() del ruteo. A veces depende del contexto, pero si bien la función de la pregunta 2 ya usa (si es que usaron) la función misterio(), hay raras ocasiones en que es mejor implementar la función misterio () de forma aislada para esta pregunta. (NO ES EL CASO PARA ESTE CERTAMEN).

El propósito de esta pregunta es que ustedes sean capaces de armar un código repetitivo que use la función que ya programaron y que termine bajo una condición (Bucle While)
"""
#Código principal
umbral = int(input("Ingrese valor umbral: "))
#Crearé una variable flag que únicamente almacenara un valor booleano que determina si el bucle continua o no:
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
        
        #Prefiero hacerlo con un if aparte en vez de un elif por la cantidad de casos "bordes" o "raros"que se podrian presentar
        if promedio < h_promedio_min:
            h_promedio_min = promedio

print("Humedad promedio máxima:", h_promedio_max)
print("Humedad promedio mínima:", h_promedio_min)
