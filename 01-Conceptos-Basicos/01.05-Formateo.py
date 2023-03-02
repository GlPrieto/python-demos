#####################################################################
# Formateo                                                          #
#####################################################################
# Cadenas y Número                                                  #
#####################################################################

mensaje = "Mundo"

# Formateando cadenas de texto
print("Hola " + mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))
print(f"Hola {mensaje} !!!")

# Formateando números
numero = 10 / 3
print(numero)
print("Hola {n:1.2f} !!!".format(n=numero))

# Ejemplos variados
mensaje = "Gloria"
print("Hola " + mensaje + " !!")
print("Hola {} !!".format(mensaje))
print("Hola {s} !!".format(s=mensaje))
print(f"Hola {mensaje} !!")
print("Hola {mensaje} !!")
resultado = "Hola {s} !!".format(s=mensaje)
print(resultado)
print("")
numero = 15 / 7
print(numero)
print("Número: {n}".format(n=numero))
resultado = "Número: {n:1.2f}".format(n=numero)
print(resultado)
