diccionario = {
    "nombre": "lady",
    "apellido": "vega",
    "suscriptores": 1860
}

#obteniendo las claves
for key in diccionario:
    print(f"la clave es: {key}")


#Recorriendo diccionario con items() para obtener las claves y los valor
for datos in diccionario.items():
   key = datos[0]
   value = datos[1]
   print(f"la claves es: {key} y el valor es: {value}")

