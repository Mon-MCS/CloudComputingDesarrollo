# Ejercicios de Ficheros

### 1 - Lista de hombres y mujeres

Crear un programa en Python para generar aleatoriamente una lista de 100 elementos que representan el género de las personas: "H" para hombres y "M" para mujeres. 

Llamar a una función llamada "ClasificarGenero" pasando la lista de personas como argumento. La función "ClasificarGenero" clasifica y cuenta la cantidad de hombres y mujeres en la lista, calcula el porcentaje de hombres y mujeres.

```
personas=[]
for n in range(1,101):
    genero=randint(0,1) #0 para mujeres y el 1 para hombres
    if (genero ==1):
        personas.append("H")
    else:
        personas.append("M")
```

**NOTA:** Puede optimizar el código anterior utilizando compresión de listas.

Deberá complementar su programa en Python para que cumpla con las siguientes condiciones:

- Mostrar una opción para generar la lista aleatoria  con datos de los 100 hombres 
- Mostrar una opción para recuperar la lista del fichero en disco (si existe) o generar una nueva lista.
- Mostrar con la lista generada o recuperada del disco las siguientes opciones estadísticas:
  - Numero de Hombres
  - Numero de Mujeres
  - Porcentaje de Hombres y Porcentaje de Mujeres
- (Opcional) Realice la opción para que el resultado de las opciones estadísticas se puedan guardar en un fichero json.

### 2 - Lista de personas para por edades.

Crear un programa en Python que genere una lista aleatoria de 100 personas, contar cuántas personas tienen 18 años o más, clasificar la lista de personas por edades procesar las siguientes estadísticas:

- Número de personas con 18 o más años: Este número indica cuántas personas en la lista tienen 18 años o más. 
- La edad más alta: Este número indica la edad más alta presente en la lista de personas. 
- La edad más baja: Este número indica la edad más baja presente en la lista de personas. 
- Clasificación por edades: En este apartado muestre la cantidad de personas que tienen cada edad presente en la lista, expréselo como un porcentaje del total de personas en la lista. Genere un nuevo diccionario para clasificar las edades y contar el número de personas correspondiente a cada edad.

```
personas=[]
for n in range(1,101):
    personas.append(randint(0,125))
```

**NOTA:** Puede optimizar el código anterior utilizando compresión de listas.

Deberá completar su programa en Python para que cumpla con las siguientes condiciones:

- Mostrar una opción para generar la lista aleatoria y almacenarla en disco.
- Mostrar una opción para recuperar la lista del fichero en disco (si existe) o generar una nueva lista.
- Mostrar con la lista generada o recuperada del disco las siguientes opciones estadísticas:
  - Número de personas con 18 o más años.
  - La edad más alta.
  - La edad mas baja.
  - Clasificación por edades.
- (Opcional) Realice la opción para que el resultado de las opciones estadísticas se puedan guardar en un fichero json.

## 3 - Lista de Personas

Crear un programa en Python que generar un conjunto de datos aleatorios que representan a 100 personas, con una edad y género aleatorios para cada una. 

```
personas = []
for _ in range(100):
    genero = "F" if randint(0, 1) == 0 else "M"
    edad = randint(0, 120)
    persona = {"genero": genero, "edad": edad}
    personas.append(persona)
```

**NOTA:** Puede optimizar el código anterior utilizando compresión de listas.

**NOTA 2:** Debe importar el módulo que contiene `randint`

Deberá completar su programa en Python para que cumpla con las siguientes condiciones:

- Mostrar una opción para generar la lista aleatoria y almacenarla en disco.

- Mostrar una opción para recuperar la lista del fichero en disco (si existe) o generar una nueva lista.

- Mostrar con la lista generada o recuperada del disco las siguientes opciones estadísticas:

  - Contar el número de mujeres mayores de edad (con edad mayor o igual a 18) y mostrarlo

  - Contar el número de hombres menores de edad (con edad menor a 18) y mostrarlo.

  - Encontrar la edad menor entre los hombres y mostrarlo.

  - Encontrar la edad menor entre las mujeres y mostrarlo.

  - Calcular el promedio de edad de los hombres y mostrarlo.

  - Calcular el promedio de edad de las mujeres y mostrarlo.

- (Opcional) Realice la opción para que el resultado de las opciones estadísticas se puedan guardar en un fichero json.

## 4 - Temperatura mensual de 20 ciudades

Crear un programa en Python que genera un diccionario de `ciudades` que contengan la temperatura media anual de cada una de las ciudades en el conjunto `NombreCiudades`. 

Para cada ciudad en `NombreCiudades`,  deberá generar la temperatura media anual calculando la suma de las temperaturas mensuales.

```
NombreCiudades={"Madrid","Barcelona","Sevilla","Malaga","Cordoba","Toledo","Valencia","Bilbao","Salamanca","Palma","Caceres","Segovia","Saragoça ","Cuenca","Alicante","Las Palmas","Avila","Merida","Granada","Murcia"}
ciudades= dict()
for i in NombreCiudades:
    media_temperaturas=0 
    for j in range (0,12):
        media_temperaturas+=randint(-10,40)
    ciudades[i]=media_temperaturas/12
```

**NOTA:** Puede optimizar el código anterior utilizando compresión de diccionarios.

El programa deberá ordenar el diccionario `ciudades` por su valor (es decir, la temperatura media anual) en orden descendente.

Deberá completar su programa en Python para que cumpla con las siguientes condiciones:

- Mostrar una opción para generar el diccionario de forma aleatoria y almacenarlo en disco.
- Mostrar una opción para recuperar el diccionario del fichero en disco (si existe) o generar un nuevo diccionario.
- Mostrar con la lista generada o recuperada del disco las siguientes opciones estadísticas:
  - Encontrar la(s) ciudad(es) con la temperatura media anual más alta
  - Encontrar la(s) ciudad(es) con la temperatura media anual más baja
  - Todas las ciudades en orden descendente de temperatura media anual.
- (Opcional) Realice la opción para que el resultado de las opciones estadísticas se puedan guardar en un fichero json.

