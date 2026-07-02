from flask import jsonify, Blueprint, request
from Entidades.sucursal import sucursales

paciente_bp = Blueprint('paciente', __name__)

pacientes = {
    501: {"id": 501, "nombre_paciente": "Carlo", "dui_paciente": "12345678-9", "telefono": "8923-1232", "id_sucursal": sucursales[201]["id"]}
}

@paciente_bp.get("/paciente")
def mostrar_pacientes():
    return jsonify(list(pacientes.values()))

@paciente_bp.get("/paciente/<int:id>")
def obtener_paciente(id):
    paciente = pacientes.get(id)

    if paciente:
        return jsonify(paciente)
    return jsonify({"error": "Este paciente no ha sido registrado en el sistema"})

@paciente_bp.post("/paciente")
def agregar_paciente():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion sobre el paciente"})
    if "nombre_paciente" not in datos or "dui_paciente" not in datos or "telefono" not in datos or "id_sucursal" not in datos:
        return jsonify({"error": "Los campos: nombre_paciente, dui_paciente, telefono y id_sucursal son requeridos para el registro"})
    
    nuevo_id = max(pacientes.keys()) + 1

    pacientes[nuevo_id] = {
        "id": nuevo_id,
        "nombre_paciente": datos["nombre_paciente"],
        "dui_paciente": datos["dui_paciente"],
        "telefono": datos["telefono"],
        "id_sucursal": datos["id_sucursal"]
    }

    return jsonify(pacientes[nuevo_id]), 201
