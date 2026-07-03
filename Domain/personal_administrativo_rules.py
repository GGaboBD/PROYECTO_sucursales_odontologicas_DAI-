# Reglas de negocio - Personal Administrativo

class PersonalAdministrativoRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el empleado")
        if "nombre" not in datos or "id_rol" not in datos or "id_sucursal" not in datos:
            raise ValueError("Los campos nombre, id_rol e id_sucursal son requeridos")
        if not datos["nombre"].strip():
            raise ValueError("El nombre no puede estar vacío")
        if not datos["id_rol"]:
            raise ValueError("El id_rol no puede estar vacío")
        if not datos["id_sucursal"]:
            raise ValueError("El id_sucursal no puede estar vacío")
