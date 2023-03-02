# Ejercicios resueltos en python
1. Calculo de la edad

   - Calcular la edad
   - Mostrar si es mayor de edad
   - Si no es mayor de edad, mostrar los años que le faltan

    Para realizar este ejercicio será necesario importar datetime:

    ```python
    from datetime import datetime
    ```
    Las siguientes líneas son para obtener la fecha actual del sistema y pedir al usuario que indique una fecha.
    ```python
    today = datetime.now().date()
    strBirthDay = input("Esccribe tu fecha de nacimiento: ")
    ```
    Al introducir los datos en la consola podría darse algún fallo de formato, por lo que es recomendable controlar dicha excepción, para ello, se pondría la siguiente lógica, dentro de un try.

    Como lo que se obtiene a partir de un input es de un tipo de dato distinto (str), será necesario aplicarle conversión a la fecha dada. Una forma de hacerlo es la siguiente:

    ```python
    birthDay = datetime.strptime(strBirthDay, "%d-%m-%Y").date()
    ```
    Teniendo la fecha que el sistema entiende como la actual y la fecha de cumpleaños del usuario, solo nos queda hacer la siguiente operación para obtener la edad:

    ```python
    age = today.year - birthDay.year
    ```
    Una vez obtenida la edad, se puede añadir una comprobación, usando if/else, para ver si es o no mayor de edad. En este caso doy por echo que la mayoría de edad es a los 18, pero soy consciente de que podría variar en otros sitios.
    ```python
    if ( age >= 18): 
        print("Es mayor de edad")
    else:
        print(f"Aun falta para cumplir la mayoría de edad {18 - age} años")
    ```
    En este caso solo tuve en cuenta los años, pero podría hacerse más exacto comprobando también meses y días.

    &nbsp;

    > [Ejercicio 1 completo](https://github.com/GlPrieto/python-demos/blob/main/01-Conceptos-Basicos/Ejercicios/01.CalcularEdad.py)

    &nbsp;

2. Calculo de la velocidad

   - Calcular la velocidad en km/h
   - La información la tenemos en metros y minutos
   - Mostrar la velocidad en km/h y si es alta, baja o moderada
   - Alta por encima de 75km/h; Baja por debajo de 30km/h; el resto moderada

    &nbsp;

    Para la resolución de este ejercicio se podría pedir al usuario que nos diese un valor de velocidad en metros por minuto:

    ```python
    strSpeed = input("Introduzca un valor de velocidad en metros por minuto: ")
    ```
    Al pedir que se introduzca un valor por consola, esto siempre nos devolverá una cadena, por lo que para obtener el resultado deseado habrá que hacer la conversión en algún punto. En mi caso opté por realizarla nada más obtener el valor y transformarlo en un entero.
    
    ```python
    speedM = int(strSpeed)
    ```

    Tras esto una cosa que faltaría responder sería ¿Cuántos Kilometro por hora hay en 1 Metro por minuto? Para ello yo usé la siguiente formula:

    > 1 Metro por minuto `[m/min]` = 0,06 Kilometro por hora `[km/h]`


    ```python
    speedKm = speedM * 0.06
    ```

    Lo que faltaría en este punto sería determinar si se considera una velocidad alta, baja o moderada. Una posible solución sería:

    ```python
    if ( speedKm > 75): 
        print(f"La velocidad {speedKm} es alta")
    elif (speedKm < 30):
        print(f"La velocidad {speedKm} es baja")
    else:
        print(f"La velocidad {speedKm} es moderada")
    ```
    &nbsp;

    > [Ejercicio 2 completo](https://github.com/GlPrieto/python-demos/blob/main/01-Conceptos-Basicos/Ejercicios/02.CalcularVelocidad.py)

&nbsp;

3. Tabla de multiplicar

    - Mostrar la tabla de multiplicar del número indicado por el usuario
    - Resolver con un FOR y también con un WHILE
    
    &nbsp;

    En este ejercicio se pide mostrar la tabla de multiplicar de un número dado por un usuario.

    ```python
    number = input("Introduzca el número del que quiera obtener la tabla de multiplicar: ")
    ```

    Una solución que muestre la tabla de un número mediante FOR sería:

    ```python
    for factor in range(1,11):
        print(f"Número {int(number)} x {factor} = {int(number)*factor}")
    ```
    Para el caso de WHILE habría que indicar previamente un valor inicial, en este caso lo llamaré `factor`:

    ```python
    factor = 0
    while (factor <= 10):
        print(f"Número {int(number)} x {factor} = {int(number)*factor}")
        factor += 1 
    ```
    &nbsp;

    > [Ejercicio 3 completo](https://github.com/GlPrieto/python-demos/blob/main/01-Conceptos-Basicos/Ejercicios/03.TablaDeMultiplicar.py)

    &nbsp;
