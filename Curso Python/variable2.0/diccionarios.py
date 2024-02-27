#Creando diccionarios con didct()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]): "jajaja"}

#creando diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido", "suscriptores"])





print(diccionario)