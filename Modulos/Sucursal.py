class Servicio:
    def __init__(self, id_servicio: str, descripcion_servicio: str, costo_servicio: float):
        self.id_servicio = id_servicio
        self.descripcion_servicio = descripcion_servicio
        self.costo_servicio = costo_servicio # Requerido por diagrama

    def to_dict(self):
        return {
            "id_servicio": self.id_servicio,
            "descripcion_servicio": self.descripcion_servicio,
            "costo_servicio": self.costo_servicio
        }