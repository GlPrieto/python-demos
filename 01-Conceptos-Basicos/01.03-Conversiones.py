#####################################################################################
# Conversiones                                                                      #
#####################################################################################
#                                                                                   #
# Realizando conversiones sobre a, b, c y temp                                      #
#                                                                                   #
#####################################################################################

# Inicialización de variables
a = 5
b = "25"
c = "25.7"
temp = "Hola"

# Conversión alfanúmerico (STR) valores númericos (INT, FLOAT)
print("Número: " + str(a))
print("")

# Conversión númericos (INT, FLOAT) valores alfanúmericos (STR)
print(f"Número: {b}")
print(type(b))
print(f"Número: {int(b)}")
print(type(int(b)))
print("")
print(f"Suma: {b + c}")
print(type(b + c))
print(f"Suma: {int(b) + float(c)}")
print(type(int(b) + float(c)))
print(int(b))
print(float(c))
print("")
print(int(b) + int(float(c)))
print(type(int(b) + int(float(c))))
print("")