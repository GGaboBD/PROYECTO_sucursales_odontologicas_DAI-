from datetime import datetime

class Venta:
    def __init__(self, id_ventas: str, fecha_venta: datetime, monto_venta: float, id_sucursal: str):
        self.id_ventas = id_ventas
        self.fecha_venta = fecha_venta
        self.monto_venta = monto_venta # Double
        self.id_sucursal = id_sucursal # FK

    def to_dict(self):
        return {
            "id_ventas": self.id_ventas,
            "fecha_venta": self.fecha_venta.strftime("%Y-%m-%d"),
            "monto_venta": self.monto_venta,
            "id_sucursal": self.id_sucursal
        }