class ServicioRules:
    @staticmethod
    def validar_creacion(datos):
        if not datos:
            raise ValueError("Debe enviar información sobre el servicio")
        
        # Validación de campos obligatorios
        if "nombre" not in datos or "precio" not in datos:
            raise ValueError("Los campos nombre y precio son requeridos")
        
        if not datos["nombre"].strip():
            raise ValueError("El nombre del servicio no puede estar vacío")
            
        # El precio debe ser un valor positivo
        if not isinstance(datos["precio"], (int, float)) or datos["precio"] <= 0:
            raise ValueError("El precio del servicio debe ser mayor a cero")