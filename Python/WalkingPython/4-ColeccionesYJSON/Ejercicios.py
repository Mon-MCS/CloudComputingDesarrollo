""" 
En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a 
diferentes sesiones de clase. La información se encuentra en un diccionario 
donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.
"""
asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

# 1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.

# Recorriendo los valores del diccionario y añadiendo su valor a un conjunto 
# sesionesTotales = set()
# for sesiones in asistencias.values():
#     sesionesTotales.update(sesiones)
# print(f"La cantidad totales de sensiones a las que asistieron Ana y Luis es {len(sesionesTotales)} y son las siguientes sesiones {sesionesTotales}")

# Recorriendo cada uno de los valores del diccionario y añadiendo su valor a un conjunto 
# sesionesTotales = set()
# for sesiones in asistencias.values():
#     for sesion in sesiones:
#         sesionesTotales.add(sesion)
# print(f"La cantidad totales de sensiones a las que asistieron Ana y Luis es {len(sesionesTotales)} y son las siguientes sesiones {sesionesTotales}")

asistenciasAna = set(asistencias["Ana"])
asistenciasLuis = set(asistencias["Luis"])
sesionesTotales = asistenciasAna.union(asistenciasLuis)
print(f"La cantidad totales de sensiones a las que asistieron Ana y/o Luis es {len(sesionesTotales)} y son las siguientes sesiones {sesionesTotales}")

# 2. Mostrar las sesiones a las que asistieron ambos alumnos.

# Creando un nuevo diccionario de asistencias donde los valores están dados por conjuntos
# asistenciasConjunto = asistencias
# for persona,sesiones in asistenciasConjunto.items():
#     asistenciasConjunto[persona]=set()
#     for sesion in sesiones:
#         asistenciasConjunto[persona].add(sesion)
# print(asistenciasConjunto)
# print(f"Las sesiones a las que asistieron ambos alumnos son {asistenciasConjunto['Ana'].intersection(asistenciasConjunto['Luis'])})")

asistenciasAna = set(asistencias["Ana"])
asistenciasLuis = set(asistencias["Luis"])
asistenciasComunes = asistenciasAna.intersection(asistenciasLuis)
print(f"Las sesiones a las que asistieron ambos alumnos son {asistenciasComunes})")

# 3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.
asistenciasAna = set(asistencias["Ana"])
asistenciasLuis = set(asistencias["Luis"])
asistenciasComunes = asistenciasAna.intersection(asistenciasLuis)
asistenciasUnAlumno = set()
asistenciasUnAlumno.update(asistenciasAna-asistenciasComunes)
asistenciasUnAlumno.update(asistenciasLuis-asistenciasComunes)
print(f"Sesiones a las que asistió uno de los alumnos pero no los dos {asistenciasUnAlumno}")

# 4. Mostrar las sesiones a las que asistió Ana pero no Luis.

asistenciasSoloAna = asistenciasAna-asistenciasLuis
print(f"Sesiones a las que asistió Ana pero no Luis {asistenciasSoloAna}")

# 5. Mostrar las sesiones a las que asistió Luis pero no Ana.

asistenciasSoloLuis = asistenciasLuis-asistenciasAna
print(f"Sesiones a las que asistió Luis pero no Ana {asistenciasSoloLuis}")


