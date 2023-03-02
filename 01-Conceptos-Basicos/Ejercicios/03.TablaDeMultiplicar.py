#######################################################################
# Requerimientos funcionales:
#
#   -> Mostar la tabla de multiplicar del número indicado por el usuario
#   -> Resolver con un FOR y también con un WHILE
#######################################################################
#Multiplication table

number = input("Introduzca el número del que quiera obtener la tabla de multiplicar: ")
print("")

# FOR
try:
    print("Inicio bloque FOR")
    print("")
    for factor in range(1,11):
        print(f"Número {int(number)} x {factor} = {int(number)*factor}")
    print("")
    print("Fin bloque FOR")
except:
    print("No se puede calcular porque el formato no es válido")

# WHILE
try:
    factor = 0
    print("")
    print("Inicio DEL WHILE")
    print("")
    while (factor <= 10):
        print(f"Número {int(number)} x {factor} = {int(number)*factor}")
        factor += 1
    print("")
    print("Fin DEl WHILE")
    print("")
except:
    print("No se puede calcular porque el formato no es válido")