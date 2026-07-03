class Servicio:
    def __init__(self, id_servicio: str, nombre: str, descripcion: str = ""):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.descripcion = descripcion

    def validar_datos(self):
        if not self.id_servicio or not str(self.id_servicio).strip():
            raise ValueError("El id del servicio no puede estar vacío")
        if not self.nombre or not str(self.nombre).strip():
            raise ValueError("El nombre del servicio no puede estar vacío")

    def registrar_servicio(self, servicios):
        self.validar_datos()
        servicios[self.id_servicio] = self.to_dict()
        return servicios

    def to_dict(self):
        return {
            "id_servicio": self.id_servicio,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
        }

    def __str__(self):
        return f"Servicio({self.id_servicio}, {self.nombre})"
