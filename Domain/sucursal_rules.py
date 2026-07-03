# Reglas de negocio - Sucursal

class SucursalRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre la sucursal")
        if "nombre" not in datos or "direccion" not in datos or "telefono" not in datos:
            raise ValueError("Los campos nombre, direccion y telefono son requeridos")
        if not datos["nombre"].strip():
            raise ValueError("El nombre de la sucursal no puede estar vacío")
        if not datos["direccion"].strip():
            raise ValueError("La dirección no puede estar vacía")
        if not datos["telefono"].strip():
            raise ValueError("El teléfono no puede estar vacío")
        nombres = [s["nombre"].lower() for s in sucursales_existentes]
        if datos["nombre"].lower() in nombres:
            raise ValueError("Ya existe una sucursal con ese nombre")