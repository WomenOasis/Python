#if anidados y else if (elif)
ingreso_mensual = 1200

if ingreso_mensual > 10000:
    print("Estas bien en cstados unidos")
elif ingreso_mensual > 4000:
    print("Estas bien colombia")
elif ingreso_mensual > 200:
    print("estas bien en choco")
else: 
    print("eres de muy bajo recursos")

    
ingreso_mensual = 72000
gasto_mensual = 20000

if ingreso_mensual > 20000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien gastando")
    else:
        print("Estas gastando mas de la cuenta")
        
elif ingreso_mensual > 500:
    print("Estas bien en venezuela")
elif ingreso_mensual > 200:
    print("Estas bien en choco")
else:
    print("Busca estrategias para ganar un poco mas")