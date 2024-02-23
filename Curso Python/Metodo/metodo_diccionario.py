#se puede como letras y numeros (nombre o 0)
diccionario = {
    "nombre" : "women",
    "apellido" : "oasis",
    "suscritores" : 1735
}

#devuelve las claves ejm(nombre, apellido, suscritores) tambien nos sirve para iterar
claves1 = diccionario.keys()

#get es un metodo que puede acceder una propiedad particular de un objeto (obteniendo un elemento con ge()) (si no encuentra nada el programa continua)
claves2 = diccionario.get("nombre")


print(claves2)