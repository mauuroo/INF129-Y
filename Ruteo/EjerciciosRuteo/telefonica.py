
def misterio(cadena, n, d):
    i = 0
    c1 = 0
    c2 = 0
    j = 0
    while i < len(cadena):
        
        if cadena[i] == "+":
            if d:
                c1 = i

        elif cadena[i] == "-":
            if d:
                c2 = i
            else:
                c1 = i

        elif cadena[i] == "|":
            if not d:
                c2 = i
            j += 1

        
        if n == (j - 1):
            return cadena[c1 + 1: c2]
        
        i += 1 


cadena = "|+56-940062145|+595-981 326746|+1-415 345 6789|"

#Aclaración -> Si hacemos el print() y dentro colocamos una función, simplemente imprimira el valor que retorna dicha función
print(misterio(cadena, 2, False))