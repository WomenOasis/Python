#creando una lista  con list()
lista = list([ 19, 27,True, False])
resultado = len(lista) # devuelve la cantidad de elemento de la lista

cadena = "hola"
resultado = len(cadena)# devuelve el numero de caracteres de una cadena 

#agragando un elemento a la lista
lista.append(56)

#agregando un elemento a la lista en un indicen especifico 
#lista.insert(2, "oasis")

#agregando varios elementos a la lista
lista.extend([False, 2030]) #se pasa dentro de los corchetes 

#eliminando un elemento de la lista (por su indice)
print(len(lista))

lista.pop(0)#-1 para eliminar el ultimo, -2 para eliminar el anteultimo y asi sucesivamente 

#removimiendo un elemento de la lista por su valor
# #lista.remove("women")

#eliminando todos los elementos de la lista

#lista.clear()

#ordenando la lista ( si usamos el parametro reverse = true lo ordena en reversa)
#lista.sort()
# no funciona si la lista tiene cadena de tecto 
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(27)

print(elemento_encontrado)
