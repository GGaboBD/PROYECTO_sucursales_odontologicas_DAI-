# Reglas de negocio - Rol

class RolRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el rol")
        if "nombre" not in datos or "descripcion" not in datos:
            raise ValueError("Los campos nombre y descripcion son requeridos")
        if not datos["nombre"].strip():
            raise ValueError("El nombre del rol no puede estar vacío")
        if not datos["descripcion"].strip():
            raise ValueError("La descripción del rol no puede estar vacía")
        if not isinstance(datos["id_rol"], int) or datos["id_rol"] <= 0:
            raise ValueError("El id_rol debe ser un número entero positivo")
    
