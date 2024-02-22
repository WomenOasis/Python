cadena1 = "hola soy women"
Cadena2 = "Bienvenidos oasis"


#print(dir(cadena1))


#CONVIERTE A MAYUSCULA
mayus = cadena1.upper()

#CONVIERTE EN MINUSCULAA
minus = cadena1.lower()
 
 
#primer letra mayuscula
primera_letra_mayus = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay concidencias devuelve -1
busqueda_find = cadena1.find("hola soy women ") 

#buscamos una cadena en otra cadena, si no hay conicidencias lanza una excepcion error
busqueda_index = cadena1.index("a")

#si es numerico, devolvemos true, sino devolvems falsee
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos true
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida 
contar_coincidencias = cadena1.count("o")

print(contar_coincidencias)

