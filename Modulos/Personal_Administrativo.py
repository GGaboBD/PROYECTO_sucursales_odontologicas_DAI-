class PersonalAdministrativo:
    def __init__(self, id_personal_administrativo: str, nombre_personal_administrativo: str, id_rol: str, id_sucursal: str):
        self.id_personal_administrativo = id_personal_administrativo
        self.nombre_personal_administrativo = nombre_personal_administrativo
        self.id_rol = id_rol
        self.id_sucursal = id_sucursal

    def to_dict(self):
        return {
            "id_personal_administrativo": self.id_personal_administrativo,
            "nombre_personal_administrativo": self.nombre_personal_administrativo,
            "id_rol": self.id_rol,
            "id_sucursal": self.id_sucursal
        }