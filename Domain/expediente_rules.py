# Reglas de negocio - Expediente

class ExpedienteRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el expediente")
        campos_requeridos = [
            "id_paciente",
            "fecha_apertura",
            "alergias_medicamentos",
            "enfermedades_existentes",
            "notas_medicas"
        ]
        for campo in campos_requeridos:
            if campo not in datos:
                raise ValueError(f"El campo {campo} es requerido")
        if not datos["id_paciente"]:
            raise ValueError("El id_paciente no puede estar vacío")
        if not datos["fecha_apertura"].strip():
            raise ValueError("La fecha de apertura no puede estar vacía")
