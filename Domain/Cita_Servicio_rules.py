class CitaServicioRules:
    @staticmethod
    def validar_asignacion(datos):
        if not datos:
            raise ValueError("Debe enviar información de la relación cita-servicio")
        
        # Ambos IDs son necesarios para crear la relación
        if "id_cita" not in datos or "id_servicio" not in datos:
            raise ValueError("Los campos id_cita e id_servicio son requeridos")
            
        if not datos["id_cita"] or not datos["id_servicio"]:
            raise ValueError("Los identificadores de cita y servicio no pueden estar vacíos")