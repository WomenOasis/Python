cadena1 = "hola, soy women"
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
contar_coincidencias = cadena1.count("a")

#contar cuantos caracteres tiene una cadena (cuantas letras)
contar_caracteres = len(cadena1)

#verficamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("hola")

#verficamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("en")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
# reemplaza un pedazo por la cadena dada, por otra dada
cadena_nueva = cadena1.replace("women", "oasis")
cadena_nueva_2 = cadena_nueva.capitalize()

#separar cadena con la cadena que le pasemos (es una lista)
cadena_separada = cadena1.split(",") 


print(type(cadena_separada))
