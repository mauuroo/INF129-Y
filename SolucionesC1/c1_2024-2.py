"""
Cómo siempre, una de las condiciones a considerar para el certamen es el hecho de que ustedes tendrán que hacerlo en papel. Por lo que antes de empezar a programar con ideas desordenadas y organizarlas en el proceso, lo recomendable es que ustedes antes de siquiera escribir código tengan claro que datos necesitan para implementar la función que les solicitan, con esto no me refiero a los argumentos de entrada de la función, sino a lo que ustedes deben extraer mediante distintas tecnicas a la entrada de la función, para luego implementar lo que les solicitan.
"""


#Pregunta 2
"""Para esta pregunta notar que siempre les dejaran el apartado "Nota:" en el cual les mencionan que pueden hacer uso de la función misterio del ruteo para implementar la solución. En todos los certamenes que he revisado se puede usar esta función para simplificar nuestra implementación, sin embargo no es el caso para este certamen en concreto. En su lugar nos indican que entender su funcionamiento puede ser útil para hacer nuestra implementación de esta pregunta. (en el desarrollo queda claro el por qué)
"""

#Notar que para esta pregunta nos mencionan un dato bastante importante que nos simplificara bastante el desarrollo de la pregunta, nos menciuonan "La cantidad de flores a comer, son de un dígito"


#Solución 1
def comer(plantacion, plan, inicio):
    flores_comidas = 0
    i = 0
    pos_actual = inicio #La pos actual inicia donde comienza el ave

    while i < len(plan):
        f = plan[i:i+3] #Variable auxiliar

        if f[1] == "I": #Leemos el movimiento
            if pos_actual - int(f[0]) < 0: #Nos salimos de rango
                pos_actual = 0 #Última posición válida
            else: #Posición válida
                pos_actual -= int(f[0])
            
        else: #Es derecha el movimiento
            if pos_actual + int(f[0]) >= len(plantacion): #Estamos fuera de rango
                pos_actual = len(plantacion) - 1 #Última posición válida

            else: #Posición válida
                pos_actual += int(f[0])
        
        if int(plantacion[pos_actual]) < int(f[2]): #No hay suficientes flores
            flores_comidas += int(plantacion[pos_actual]) #Comemos antes de actualizar

            plantacion = plantacion[:pos_actual] + "0" + plantacion[pos_actual + 1:]


        
        else: #Hay suficinetes flores
            flores_comidas += int(f[2]) #Comemos antes de actualizar

            plantacion = plantacion[:pos_actual] + str(int(plantacion[pos_actual]) - int(f[2])) + plantacion[pos_actual + 1:]


        i += 4

    return flores_comidas


#Pregunta 3
plan = input("Ingrese el plan de comida: ")
ingesta_min = int(input("Ingrese la ingesta mínima para el día: "))
num_plantaciones = int(input("Ingrese el número de plantaciones a analizar: "))

i = 0

plantacion_max = 0
flores_max = -10000 #Un número muy pequeño

while i < num_plantaciones:
    print("Plantación:", i + 1) #AL usar , ya hay espacio
    plantacion = input("Ingrese la plantación: ")
    inicio = int(input("Ingrese la casilla de inicio: "))

    flores_comidas = comer(plantacion, plan, inicio)
    if flores_comidas >= ingesta_min:
        print("Cumple! Come", flores_comidas)
    
    else:
        print("No cumple con la ingestia mínima, apenas come", flores_comidas)
    
    if flores_comidas > flores_max:
        flores_max = 0
        plantacion_max = i + 1

    i += 1 #Recordar actualizar la variable

print("La plantación", plantacion_max, "es la que permite comer más")

 
