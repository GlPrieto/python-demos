#######################################################################
# Requerimientos funcionales:
#
#   -> Calcular la velocidad en km/h
#   -> La información la tenemos en metros y minutos
#   -> Mostrar la velocidad en km/h y si es alta, baja o moderada
#   -> Alta por encima de 75km/h; Baja por debajo de 30km/h; el resto moderada
#######################################################################

strSpeed = input("Introduzca un valor de velocidad en metros por minuto: ")

try:
    speedM = int(strSpeed)
    print("")

    # Un metro por minuto [m/min] es igual a 0,06 Kilometro por hora [km/h]
    speedKm = speedM * 0.06
    print(f"La velocidad dada ha sido: {speedKm}")

    if ( speedKm > 75): 
        print(f"La velocidad {speedKm} es alta")
    elif (speedKm < 30):
        print(f"La velocidad {speedKm} es baja")
    else:
        print(f"La velocidad {speedKm} es moderada")

except:
    print("No se puede calcular porque el formato no es válido")