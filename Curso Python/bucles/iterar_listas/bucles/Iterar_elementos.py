#con for y in hacer el bucle 
#iterar es repetir 
animales = ["gato","perro","loro","cocodrilo"]
numeros = [10,62,12,72]
 

# Recorriendo la lista de animales 
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#reocrriendo la lista numeros y multiplicando cada valor pór 10     
for numero in numeros: 
    resultado = numero *10
    print(resultado)
 
#iterando dos lists del mismo tamaño y al mismo tiempo 
for numer, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animales}")

#
for num in range(10,20):
    print(num)
    

#forma no op´tima de recorrer una lista 
for num in range(len(numeros)):
    print(numeros[num])


#forma correcta de recorrer uyna lista con su indice
for num in enumerate(numeros):
    indice = (num[0])
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#usando un else for /else
for   numero in numeros:
    print(f"Utilizando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
    #todo lo anterior funciona exactamente igual para tuplas y listas 
    





























