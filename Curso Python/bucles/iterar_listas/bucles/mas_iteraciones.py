
#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = 'leidy vega'
numeros = [2,4,8,10]



#evitando que se coma una manzana con la sentencia cotinue
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'me voy a comer una {fruta}')
    
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:    
 print("bucle terminado")
 

#recorrer una cadena de texto

for letra in cadena:
    print(letra)
 

#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados =  [x*2 for x in numeros]
print(numeros_duplicados)