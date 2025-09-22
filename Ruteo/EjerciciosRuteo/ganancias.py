#Aclaración -> s: str es una forma de indicarle a python de que nuestro parametro 's' es de tipo string, no necesitan saber esto solo lo dejaré puesto para que sepan que en el ruteo nuestra principal parametro siempre sera de tipo string.

def misterio(s: str, a):
    i = 0
    c = 0
    flag = False

    while i < (len(s)):
        if s[i] == "$":
            flag = True
        elif s[i] == "-":
            flag = False
        elif len(s) == (i + 1):
            flag = False
            c += 1
            

        if flag:
            c += 1
        else:
            if (c - 1) == a:
                return True
            c = 0

        i += 1

    return False


cadena = "$3500-$22700-$500"
i = 3

#Aclaración -> Si hacemos el print() y dentro colocamos una función, simplemente imprimira el valor que retorna dicha función
#Aclaración -> Es importante saber distinguir entre la variable i del código global, a la variable i del código de la función, son distintos y viven en ambitos distintos
a = misterio(s=cadena, a=i)
print(a)
print(i)

#¿Que hace la función?


