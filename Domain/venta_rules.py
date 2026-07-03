# Reglas de negocio - Venta
import datetime

class VentaRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre la venta")
        if "fecha_venta" not in datos or "monto_venta" not in datos or "id_sucursal" not in datos:
            raise ValueError("Los campos fecha_venta, monto_venta e id_sucursal son requeridos")
        if not datos["fecha_venta"].strip():
            raise ValueError("La fecha de venta no puede estar vacía")
        if datos["monto_venta"] <= 0:
            raise ValueError("El monto de venta debe ser mayor a cero")
        
        fecha_venta = datetime.strptime(datos["fecha_venta"], "%Y-%m-%d")
        if fecha_venta > datetime.now():
            raise ValueError("La fecha de venta no puede ser futura")