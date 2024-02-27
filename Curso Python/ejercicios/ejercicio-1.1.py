#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max =7
otros_cursos_promedio = 4
women_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_women = 3.5

#direncia de duracion
diferencia_con_min = 100 - women_curso / otros_cursos_min * 100
diferencia_con_max = 100 - women_curso* 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 -women_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacio removido 
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_women = 100 - women_curso * 1000 // crudo_women / 10

#Mostrando las diferencias de duracion (ejercicio A)
print('----------------')
print('El curso de dalto dura:')
print(f' - El curso de women dura un {diferencia_con_min}% menos que el mas rapido')
print(f' - El curso de women dura un {diferencia_con_max}% menos que el mas lento')
print(f' - El curso de women dura un {diferencia_con_promedio}% menos que el promedio')
print('----------------')

#Mostrando la cantidad de espacios vacios que se remueven (ejercicios B)
print(f' - Un curso promeido elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f' - Este curso elimino el {tiempo_vacio_women}% de tiempo vacio')
print('----------------')

#mostrando diferencias si los cursos duraran 10 horas
print(f' - ver 10 hora de este curso equivale a ver {otros_cursos_promedio *100 // women_curso / 10} horas de otros cursos')
print(f' - ver 10 hora de otros curso equivale a ver {women_curso *100 // otros_cursos_promedio / 10} horas de este cursos')
print('----------------')
