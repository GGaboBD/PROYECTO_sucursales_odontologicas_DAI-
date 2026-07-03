class Rol:
    def __init__(self, id_rol: str, nombre_rol: str, descripcion: str):
        self.id_rol = id_rol
        self.nombre_rol = nombre_rol
        self.descripcion = descripcion

    def to_dict(self):
        return {
            "id_rol": self.id_rol,
            "nombre_rol": self.nombre_rol,
            "descripcion": self.descripcion
        }