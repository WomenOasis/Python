#Le pedimos al usuario que nos diga una grase (o varias)
frase = input('Dime un afrase y te calculo cuanto tardarias diciendolo si tuviera que decirla: ')

#creamos una lista con todas las palabras de la frase ( se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista 
cantidad_de_palabras = len(palabras_separadas)  

#en caso de que tarde mas de un minuto decirlo, le decimos que pare un poco
if ((cantidad_de_palabras/2) >60):
   print("Para flaco tampóco te pedi un testamento")#
 
#calculamos cuanto tardaria en decir las palabras y se lo decimos 
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo') 
print(f'Dalto lo diria en {cantidad_de_palabras /2*0.3} segundo en decirlo') 










