from flask import jsonify, Blueprint, request

sucursal_bp = Blueprint('sucursal', __name__)

sucursales = {
    201: {"id": 201, "nombre": "Alvincito Dental", "direccion": "Soyapango", "telefono": "8732-9122"}
}

@sucursal_bp.get("/sucursal")
def mostrar_sucursales():
    return jsonify(list(sucursales.values()))

@sucursal_bp.get("/sucursal/<int:id>")
def obtener_sucursal(id):
    sucursal = sucursales.get(id)

    if sucursal:
        return jsonify(sucursal)
    return jsonify({"error": "Esta sucursal no se ha encontrado"})

@sucursal_bp.post("/sucursal")
def agregar_sucursal():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion sobre la sucursal"})
    if "nombre" not in datos or "direccion" not in datos or "telefono" not in datos:
        return jsonify({"error": "Los campos de nombre, direccion y telefono son requeridos en el registro"})
    
    nuevo_id = max(sucursales.keys()) + 1

    sucursales[nuevo_id] = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "direccion": datos["direccion"],
        "telefono": datos["telefono"]
    }

    return jsonify(sucursales[nuevo_id]), 201