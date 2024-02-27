
#Creando un conjunto con set()
conjunto = set(["Dato 1",])

#Metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset(["dato1", "dato2"]) # frozenset nos ayuda meter un conjunto con otro conjunto  
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)


#Teoria de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}
#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1) # si son subconjuntos ya que conjunto2 tiene numeros de conjunto1, pero si es al reves no ya que conjunto 1 tiene mas cosas (numeros)
resultado = conjunto2 <= conjunto2# otra forma de verficarlo pero si tienen lo mismo biern asi sea alreves

#verificando si es un superconjunto es todo lo contrario de subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 > conjunto1 

#verificando si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)# vota true si no hay ningun numero igual 
 
print(resultado)

