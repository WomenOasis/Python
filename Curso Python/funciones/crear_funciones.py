#creando una funcion simple
def saludar():
    print("hola leidy, influencer ¿Como estas?")

#ejecutando la funcion simple 
#saludar()


#Crear una funcion que tenga parametros
'''
def saludar(nombre,sexo):
    sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
       adjetivo = "titan"
    else:
       adjetivo = "amor"
    print(f"Hola {nombre}, mi {adjetivo},¿Como estas?")

saludar("leidy", "mujer")         
saludar("pipe", "hombre")
saludar("fran", "no binario")
'''
#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2 #caracter(c)
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
passsword = (crear_contraseña_random(0))
frase = f"Tu contraseña nueva es: {passsword}"
print(passsword)