z = "Ingrese un texto en minuscula con números romanos en mayusculas: "
a = [["I",1],["X",10],["C",100]] #siempre en 0 tengo la letra y en 1 tengo el significado
f = [["V",5],["L",50],["D",500]]
b = input(z)
b = b.replace(","," , ") #remover comas y puntuacion
b = b.replace("."," . ")
c = b.split() #va a separar por espacios las palabras y las guarda en una lista
d = "" #las palabras que van a ir en el texto final

for i in range(len(c)): #va a recorrer cada uno de los elementos, recorre cada una de las palabras
    if c[i].isupper(): #isupper determina si la cadena de texto es mayuscula o minuscula
        e = [] #lista auxiliar, guarda equivalencias de los números
        for j in c[i]: #va a recorrer las letras de las palabras que estan guardadas en i
            for k in range(len(a)): #Para hacer la busqueda en la lista a
                if j == a[k][0]: #si la letra en la posicion k_0 es la letra, y 0 es la letra
                    e.append(a[k][1]) #Aqui busca el número
                    break #se encuentra la equivalencia y sigue con la siguiente letra
                if j == f[k][0]:
                    e.append(f[k][1])
                    break
        if len(c[i]) == len(e): #el tamaño de la palabra es igual al tamaño de las equivalencias encontradas
            suma = 0
            aux = e[0] # se guarda la primera equivalencia 
            for j_2 in range(1, len(e)):
                if aux >= e[j_2]:
                    suma = suma + aux
                else:
                    suma = suma - aux
                aux = e[j_2]
            suma = suma + aux
            d = d + " " + str(suma)
        else: #si el tamaño de la palabra no es igual a las equivalencias, deja la palabra tal y como esta
            d = d+" "+c[i]
    else: #si la palabra es minuscula, se deja tal como esta
        if c[i] != "," and c[i] != ".":
            d = d + " "
        d = d+c[i]+"" #Sin comas porque imprime mal
        

print(d)