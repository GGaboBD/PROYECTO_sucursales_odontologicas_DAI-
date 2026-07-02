from flask import jsonify, Blueprint, request
from Entidades.sucursal import sucursales

ventas_bp = Blueprint('ventas', __name__)


ventas = {
    101: {"id": 101, "fecha_venta": "15/6/2026", "monto_venta": 45.99, "id_sucursal": sucursales[201]["id"]}
}

@ventas_bp.get("/ventas")
def mostrar_ventas():
    return jsonify(list(ventas.values()))

@ventas_bp.get("/ventas/<int:id>")
def obtener_venta(id):
    venta = ventas.get(id)

    if venta:
        return jsonify(venta)
    return jsonify({"error": "Esta venta no se ha encontrado"})

@ventas_bp.post("/ventas")
def agregar_venta():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion sobre la venta"})
    if "fecha_venta" not in datos or "monto_venta" not in datos or "id_sucursal" not in datos:
        return jsonify({"error": "Los campos de fecha y monto son requeridos en el registro"})
    
    nuevo_id = max(ventas.keys()) + 1

    ventas[nuevo_id] = {
        "id": nuevo_id,
        "fecha_venta": datos["fecha_venta"],
        "monto_venta": datos["monto_venta"],
        "id_sucursal": datos["id_sucursal"]
    }

    return jsonify(ventas[nuevo_id]), 201

