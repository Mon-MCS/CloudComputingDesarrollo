import json

persona = {
    "nombre":"Juan",
    "edad":30,
    "ciudad":"Madrid"
}

# Convertir un objeto Python a JSON
jsonPersona = json.dumps(persona)

print(persona, type(persona))
print(jsonPersona, type(jsonPersona))

# Convertir un objeto JSON a Python

stringJSONPersona = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'
persona2 = json.loads(stringJSONPersona)
print(persona2, type(persona2))

stringPrimerJson = """
[
    {
        "nombre":"Juan",
        "edad":30,
        "estadoCivil":"Soltero",
        "pasatiempos":["leer","viajar"],
        "estudiando":true,
        "trabajando":null,
        "direccion": {
            "calle":"Calle Mayor",
            "numero":1,
            "ciudad":"Madrid"
        }
    },
    {
        "nombre":"Pedro",
        "edad":25,
        "estadoCivil":"Soltero",
        "pasatiempos":["bailar","viajar"],
        "estudiando":true,
        "trabajando":true,
        "direccion": {
            "calle":"Calle Del Soto",
            "numero":13,
            "ciudad":"Madrid"
        }
    }
]
"""
persona3 = json.loads(stringPrimerJson)
print(persona3,type(persona3))