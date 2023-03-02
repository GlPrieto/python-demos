#####################################################################
# Fecha y hora                                                      #
#####################################################################
# Trabajando con fechas                                             #
#####################################################################
#                                                                   #
#   Sintaxis: datetime.now()                                        #
#             datetime.now().date()                                 #
#             datetime.now().today()                                #
#                                                                   #
#             datetime.strptime("11-03-1998", "%d-%m-%Y").date()    #
#             print(datetime.now().strftime("%A, %d %m, %Y")        #
#                                                                   #
#####################################################################
from datetime import datetime
import time

t1 = time.time()
t2 = time.localtime(t1)
t3 = time.asctime(t2)
print(t1)
print(t2)
print(t2.tm_year)
print(t3)
print("")

# TIME devuelve la cantidad de segundos transcurridos desde el comienzo el tiempo (normalmente 01-Ene-1970 00:00:00)
print(f"Segundos desde 01-01-1970: {t1}")
print("")

# Transformar segundos en una fecha
print(f"Tupla: {t2}")
print(f"Propiedad Año: {t2.tm_year}")
print("")

# Convierte una Tupla de tiempo en una representación de fecha y hora local  
print(f"Fecha: {time.asctime(t2)}")
print("")

# Fecha y hora despues de transcurrir 14852 segundos desde 01-01-1970 00:00:00
xt = time.localtime(14852)
print("Después de pasar 14852 desde el 01-Ene-1970 a las 0:00")
print(f"la fecha es: {time.asctime(xt)}")
print("")

# Almacenamos en la variable dt1 la fecha y hora actual del sistema
dt1 = datetime.now()
print("Fecha1: ", dt1)

print("Día:", str(dt1.day).zfill(2))
print("Mes:", str(dt1.month).zfill(2))
print("Año:", dt1.year)
print("Hora:", dt1.hour)
print("Minutos:", dt1.minute)
print("Segundos:", dt1.second)
print("Milisegundos:", dt1.microsecond)

print("")

# Almacenamos en la variable dt2 la fecha actual del sistema
dt2 = datetime.now().date()
print("Fecha2: ", dt2)

print("Día:", dt2.day)
print("Mes:", dt2.month)
print("Año:", dt2.year)

print("")

# Inicialización de variables


# Convertimos un valor alfanúmerico en fecha utilizando STRPTIME
fecha = input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()

# Mostramos por pantalla una fecha formateada
print("Fecha3: ", dt3.strftime("%A, %d of %B, %Y"))

print(f"Fecha de nacimiento: {dt3}")
print("Fecha de nacimiento: ", dt3.strftime("%A, %d-%B-%Y"))


# Calculos entre fechas
años = dt1.year - dt3.year
print(f"Tienes {años} años.")

dias = dt2 - dt3
print(f"Tienes {dias.days} dias.")
print("")

print("Edad: ", dt1.year - dt3.year)
dt4 = dt2 - dt3
print(f"Tienes {dt4} días.") # Que muestre años