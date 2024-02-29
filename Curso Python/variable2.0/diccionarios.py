#Creando diccionarios con didct()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]): "jajaja"}

#creando diccionario con fromkeys() valor por defecto none
diccionario1 = dict.fromkeys(["nombre", "apellido"])

#creando diccionario con fromkeys() con dos parametros 
diccionario2 = dict.fromkeys(["nombre", "apellido"], "No se")
diccionario3 = dict.fromkeys("ABCD", "Algun valor fijo")



print(diccionario2)