#####################################################################################
# Sentencias de control                                                             #
#####################################################################################

# IF/ELIF/ELSE
#####################################################################
#                                                                   #
#   Las sentencias de decisión determinar el flujo del programa     #
#   tras evaluar una expresión de comparación.                      #
#                                                                   #
#                                                                   #
#   Sintaxis:          Es igual: a == b                             #
#                   No es igual: a != b                             #
#                     Menor que: a <  b                             #
#                 Menor o igual: a <= b                             #
#                     Mayor que: a >  b                             #
#                 Mayor o igual: a >= b                             #
#                                                                   #
#####################################################################
a = 10
b = 20

# Inicio del IF
if ( a > b ): 
    print(f"El número mayor es a: {a}")
elif ( b > a ): 
    print(f"El número mayor es b: {b}")
else: 
    print("Los números son iguales")
# Fin del IF
print("")
print("FIN DE LA EJECUCÓN")

# FOR
#####################################################################
#                                                                   #
#   Sintaxis: for [variable] in [variable colección]                #
#             print([variable])                                     #
#                                                                   #
#             for [variable] in range([inicio], [fin], [intervalo]) #
#             print([variable])                                     #
#                                                                   #
#####################################################################

for i in range(0, 100, 1):
    print(f"Número {i}")
    print("")
    
citricos = ["limón", "naranja", "pomelo", "lima", "mandarina" ]
print(citricos)
print("")
print(citricos[:2])
print("")
print(f"Número de valores: {len(citricos)}")
print("")

# Utilizamos FOR para recorrer colecciones.
for fruta in citricos:
    print(fruta)
    print("")
print("")

# Utilizamos FOR para recorrer colecciones, con RANGE establecemos un contador
# que nos da las posiciones de la colección de citricos
for i in range(0, len(citricos), 1):
    print(f"{i}: {citricos[i]}")
print("")

for i in range(len(citricos)):
    print(f"{i}: {citricos[i]}")
print("")

# Podemos utiliza FOR combinado con otras funciones como ENUMERATE que
# retorna el indice y el valor de cada elemento de la colección

for index, fruta in enumerate(citricos):
    print(f"{index}: {fruta}")
print("")

# Utilizamos FOR para recorrer colecciones.
# Cuando fruta es igual a pomelo se finaliza el for con break, por lo que no
# muestra el valor de lima ni mandarina.
for fruta in citricos:
  print(fruta)
  if fruta == "pomelo":
      break
print("")

# Utilizamos FOR para recorrer colecciones.
# Cuando fruta es igual a pomelo se cotinua el for con continue, por lo que no
# muestra el valor de líma pero si mandarina.
for fruta in citricos:
  print(fruta)
  if fruta == "pomelo":
      continue
print("")
  
# Utilizamos FOR con RANGE para establecer un contador y ejecutar
# sentencias repetidas veces.

# Ejemplo: de 0 a 99 de 5 en 5
for i in range(0, 100, 5):
    print(f"Número: {i}")
print("")

# Ejemplo: de 5 a 0 de 1 en 1
for i in range(5, 0, -1):
    print(f"Número {i}")
print("")

# Ejemplo
for x in range(0, 4, 1):
    print(f"{x}: {citricos[x]}")
#for numero in range(3)
    print()
#for 
    print()

# WHILE
#####################################################################
#                                                                   #
#   Sintaxis: while ([condición]):                                  #
#                                                                   #
#   Con while podemos ejecutar un conjunto de sentencias            #
#   siempre que la condición sea verdadera.                         #
#                                                                   #
#####################################################################

valor = 0
while (valor < 5):
    valor += 1
    if (valor == 3):
        continue    # Recordatorio: Esto se salta ese valor y sigue con la ejecución
    print(f"Valor actual: {valor}")
print("")
print("FIN DEl WHILE")
print("")

#####################################################################

citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]
index = 0

while (index < len(citricos)):
    print(citricos[index])
    index += 1

print("Fin del WHILE")
print("")

#####################################################################

index = 0

while (index < 5):
    index = index + 1                   # equivalente a valor += 1
    if (index == 2):
        break                           # también podemos utilizar continue
    print(f"El valor es {valor}.")

print("Fin del WHILE")
print("")

#####################################################################

# Como implementar un DO/WHILE de otros leguajes de programación.
# Nos aseguramos que las sentencias se ejecutan al menos una vez.

index = 0

while (True):
   print(citricos[index])
   index += 1
   if (index >= len(citricos)):
       break
   else:
        print("Fin del WHILE")

## Ejercicio con while

index = 0
while (index < len(citricos)):
    print(f"{index}: {citricos[index]}")
    index += 1
print("")
print("FIN DEl WHILE")
print("")