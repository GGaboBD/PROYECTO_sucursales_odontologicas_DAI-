from flask import jsonify, Blueprint, request

rol_bp = Blueprint('rol', __name__)

roles = {
    401:{"id": 401, "nombre_rol": "Dentista", "descripcion": "Es dentista JHJAJJA"}
}

@rol_bp.get("/rol")
def mostrar_roles():
    return jsonify(list(roles.values()))

@rol_bp.get("/roles/<int:id>")
def obtener_rol(id):
    rol = roles.get(id)

    if rol:
        return jsonify(rol)
    return jsonify({"error": "Rol no disponible"})

@rol_bp.post("/rol")
def agregar_rol():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion sobre el rol"})
    if "nombre_rol" not in datos or "descripcion" not in datos:
        return jsonify({"error": "Los campos de nombre y descripcion son requeridos en el registro"})
    
    nuevo_id = max(roles.keys()) + 1

    roles[nuevo_id] = {
        "id": nuevo_id,
        "nombre_rol": datos["nombre_rol"],
        "descripcion": datos["descripcion"]
    }

    return jsonify(roles[nuevo_id]), 201