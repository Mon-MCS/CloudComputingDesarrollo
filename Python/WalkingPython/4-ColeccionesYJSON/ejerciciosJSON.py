import json

def pythonJSON(info):
    # Convertir un objeto Python a JSON
    infoJSON = json.dumps(info)

    print(info, type(info))
    print(infoJSON, type(infoJSON))

    # Convertir un objeto JSON a Python
    stringJSONinfo = str(infoJSON)
    info1 = json.loads(stringJSONinfo)
    print(info1, type(info1))

### Programa 1: Información sobre un usuario: 
'''
El JSON generado deberá ser:
{"nombre": "Juan", "edad": 30, "email": "juan@acme.com", 
"trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}
'''

usuario = {
    "nombre":"Juan",
    "edad":30,
    "email":"juan@acme.com",
    "trabajo":{
        "empresa":"Acme Corp",
        "puesto":"Ingeniero de software"
    }
}

pythonJSON(usuario)

print("--------")
### Programa 2: Transacción financiera:
'''
El JSON generado deberá ser:
{"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, 
"tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, 
"descripcion": "Un teléfono inteligente de última generación"}}
'''
transaccion = {
    "id": 123456789, 
    "fechayhora": "2023-04-18T12:30:00Z", 
    "monto": 500.25, 
    "tipo": "compra", 
    "producto": {
        "nombre": "Smartphone", 
        "precio": 450.00, 
        "descripcion": "Un teléfono inteligente de última generación"
    }
}

pythonJSON(transaccion)
print("--------")

### Programa 3: Información medica de paciente:
'''
El JSON generado deberá ser:
{"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, 
"altura": 1.75, "historial_medico": {"alergias": ["penicilina", "mariscos"], 
"problemas_cardiacos": false, 
"medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, 
{"nombre": "Paracetamol", "dosis": "500mg"}]}, "ultima_revision": "2022-10-01", 
"proximo_turno": "2023-05-15"}
'''

paciente = {
    "nombre": "Pedro", 
    "apellido": "Pérez", 
    "edad": 45, 
    "peso": 80.5, 
    "altura": 1.75, 
    "historial_medico": {
        "alergias": ["penicilina", "mariscos"], 
        "problemas_cardiacos": False, 
        "medicamentos": [
            {"nombre": "Ibuprofeno", "dosis": "200mg"}, 
            {"nombre": "Paracetamol", "dosis": "500mg"}
            ]
        }, 
    "ultima_revision": "2022-10-01", 
    "proximo_turno": "2023-05-15"
}

pythonJSON(paciente)