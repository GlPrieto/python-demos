#####################################################################################
# Cadenas de caracteres                                                             #
#####################################################################################
#                                                                                   #
# Trabajando con Cadenas de Texto                                                   #
#                                                                                   #
#####################################################################################

# Inicialización de variables
cadena = "Hola Mundo"
print(cadena)

# Mostrar caractéres de posiones o rangos
print(cadena[2])
print(cadena[2:])
print(cadena[:6])
print(cadena[2:6])
print(cadena[-2])

print(f"Número de caractéres: {len(cadena)}")

# Funciones de objetos de tipo STR
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())
print(cadena.replace("o", "0"))
print(cadena.isdigit())
print("234".isdigit())
print(cadena.count("o"))