#####################################################################
# Zonas horarias                                                    #
#####################################################################
#                                                                   #
#  Requiere instalar el módulo PYZT: pip install pytz               #
#                                                                   #
#####################################################################

from datetime import datetime

import pytz

# Mostrar las zonas horarias disponibles
print(f"Zonas horarias: {pytz.all_timezones}")
print("")

# Mostrar la fecha actual
dt = datetime.now()
print(f"Fecha actual: {dt}")
print(f"Zona Hoararia: {dt.tzinfo}")
print("")

# Mostrar la fecha actual en la zona horario de Asia/Tokyo
tokyo = dt.now(pytz.timezone("Asia/Tokyo"))
print(f"Fecha Tokyo: {tokyo}")
print(f"Zona Hoararia: {tokyo.tzinfo}")
print("")

# Mostrar otras zonas horarias

madrid = datetime.now(pytz.timezone('Europe/Madrid'))
alaska = datetime.now(pytz.timezone('US/Alaska'))
utc = datetime.now(pytz.timezone('UTC'))
print(f"Fecha actual en Tokyo: {tokyo}")
print("")
print(f"Fecha actual en Madrid: {madrid}")
print("")
print(f"Fecha actual en Alaska: {alaska}")
print("")
print(f"Fecha actual en el meridiano: {utc}")
print("")