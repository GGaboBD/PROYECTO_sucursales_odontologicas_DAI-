class Especialidad:
    def __init__(self, id_especialidad: str, especialidad_descripcion: str):
        self.id_especialidad = id_especialidad
        self.especialidad_descripcion = especialidad_descripcion

    def to_dict(self):
        return {
            "id_especialidad": self.id_especialidad,
            "especialidad_descripcion": self.especialidad_descripcion
        }