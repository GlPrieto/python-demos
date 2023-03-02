#####################################################################
# Sentencias de Control - Try/Except/Else/Finally                   #
#####################################################################
#                                                                   #
#   try     permite controlar las excepciones producidas en un      #
#           bloque de código.                                       #
#                                                                   #
#   except  bloque de instrucciones que se ejecutan cuando se       #
#           produce una excepción.                                  #
#                                                                   #
#   else    bloque de instrucciones que se ejecutan al finalizar    #
#           el try si no se produce un excepción.                   #
#                                                                   #
#   finally bloque de instrucciones que se ejecutan siempre que     #
#           finaliza el try, except o else.                         #
#                                                                   #
#####################################################################
import sys

num1 = 0
num2 = 100
#####################################################################

print("Inicio")
try:
    num3= num1/num2
    print(f"Resultado: {num3}")
    f = open('myfile.txt')
except ZeroDivisionError as err:
    print("No se puede dividir por 0")
    print(err)
    print(type(err))
except FileNotFoundError as err:
    print("El fichero que intenta abrir no existe")
    print(err)
    print(type(err))
except:
    print("Se ha producido una excepción")
print("Fin")

###########################################################################

try:
    num3 = num2 / num1
    print(f"Número 3: {num3}")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except:
    print("Upsss Error !!!")
else:
    print("Bloque TRY finalizado correctamente")
finally:
    print("Bloque TRY o EXCEPT finalizado correctamente")
print("")

###########################################################################

try:
    num3 = num1 / num2
    print(f"Número 3: {num3}")
    f = open('myfile.txt')
except ZeroDivisionError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
    print(type(err))
except Exception as err:
    print(err)
finally:
    print("Fin")
print("")


###########################################################################
# Utilizamos RAISE para generar una Error controlable mediante Try/Except #
###########################################################################

num = "32"

try:
    if (type(num) is not int):
        raise Exception("La variable no es númerica")
except Exception as ex:
    print(ex)