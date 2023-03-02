#######################################################################
# Requerimientos funcionales:
#
#   -> Calcular la edad
#   -> Mostrar si es mayor de edad
#   -> Si no es mayor de edad, mostrar los años que le faltan
#######################################################################

from datetime import datetime

today = datetime.now().date()
strBirthDay = input("Esccribe tu fecha de nacimiento: ")
try:
    birthDay = datetime.strptime(strBirthDay, "%d-%m-%Y").date()

    age = today.year - birthDay.year
    print("Edad: ", age)
    if ( age >= 18): 
        print("Eres mayor de edad")
    else:
        print(f"Aun te falta para cumplir la mayoría de edad {18 - age} años")
except:
    print("No se puede calcular porque el formato no es válido")