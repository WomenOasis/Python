numeros = [4,7,1,42,25 ]

#encuentrando el numero mayor de una lista
numero_mas_alto = max(numeros)

#encuentrando el numero menor de una lista
numero_mas_bajo = min(numeros)

#redondeando a 6 decimales 
numero = round(12.345678,2)


#retorno false -> 0, vacio, Fale, none / True -> distinto a 0, cadena, datos no vacios 
resultado = bool(0)


#retorna True, si todos los valores son verdaderos
resultado_all = all([123,"True", [322,434]])

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)