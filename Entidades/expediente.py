from flask import jsonify, Blueprint, request
from Entidades.paciente import pacientes

expedientes_bp = Blueprint('expediente', __name__)

expedientes = {
    601: {"id": 601, "id_paciente": pacientes[501]["id"], "fecha_apertura": "01/07/2026", "alergias_medicamentos": "Alergia a Gaby", "enfermedades_existentes": "cancer", "notas_medicas": "El paciente esta bien, dejar de alta"}
}

@expedientes_bp.get("/expediente")
def mostrar_expedientes():
    return jsonify(list(expedientes.values()))

@expedientes_bp.get("/expediente/<id>")
def obtener_expediente(id):
    expediente = expedientes.get(id)

    if expediente:
        return jsonify(expediente)
    return jsonify({"error": "Este expediente no ha sido registrado en el sistema"})

@expedientes_bp.post()
def agregar_expediente():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion sobre el expediente"})
    if "id_paciente" not in datos or "fecha_apertura" not in datos or "alergias_medicamentos" not in datos or "enfermedades_existentes" not in datos or "notas_medicas" not in datos:
        return jsonify({"error": "Los campos: id_paciente, fecha_apertura, alergias_medicamentos, enfermedades_existentes y notas_medicas son requeridos en el registro"})
    
    nuevo_id = max(expedientes.keys()) + 1

    expedientes[nuevo_id] = {
        "id": nuevo_id,
        "id_paciente": datos["id_paciente"],
        "fecha_apertura": datos["fecha_apertura"],
        "alergias_medicamentos": datos["alergias_medicamentos"],
        "enfermedades_existentes": datos["enfermedades_existentes"],
        "notas_medicas": datos["notas_medicas"]
    }

    return jsonify(expedientes[nuevo_id]), 201