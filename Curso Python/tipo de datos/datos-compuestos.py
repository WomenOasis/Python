#los 5 compuestos
#varios datos juntos
#indice en que posicion esta
#array que tiene varios datos, contamos del 0 en adelante

#creando una lista (se puede modificar)
lista =["Leidy vega", "soy women",1.85, True,1234]
#print(lista[0])
#lista[2] = ["Happy"]
#print(lista[3])

#creando una tupla no se puede modificar
#tupla
tupla = ("Leidy vega", "soy women", True,1234)



#creando un conjundo (set), no se modifica ningun elemento
#no se duplia el cojunto una palabra repetid, no accede l indice
conjunto = {"Leidy vega", "soy women", True,1234,"Leidy vega"}#ese ultimo leidy veg no se repite 

#print (conjunto[3]) -> no puede acceder a ningun elemento
#print(conjunto)


#Creando un diccionario (dict)
#la estructura es key : value y se separa con comas
dictionary = {
    'name' : 'Leidy vega',
    'channel' : 'soy women',
    "i'm_excited": True,
    'height' : 1.85,
    'duplicate_date' : 'soy women'
}

print(dictionary['height'] + 2)
print(lista[2])


