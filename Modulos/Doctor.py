class Doctor:
    def __init__(self, id_doctor: str, nombre: str, jvpo_doctor: str, id_sucursal: str, id_especialidad: str):
        self.id_doctor = id_doctor
        self.nombre = nombre
        self.jvpo_doctor = jvpo_doctor
        self.id_sucursal = id_sucursal
        self.id_especialidad = id_especialidad

    def validar_datos(self):
        if not self.id_doctor or not str(self.id_doctor).strip():
            raise ValueError("El id del doctor no puede estar vacío")
        if not self.nombre or not str(self.nombre).strip():
            raise ValueError("El nombre del doctor no puede estar vacío")
        if not self.jvpo_doctor or not str(self.jvpo_doctor).strip():
            raise ValueError("El JVPO del doctor no puede estar vacío")
        if not self.id_sucursal or not str(self.id_sucursal).strip():
            raise ValueError("La sucursal del doctor no puede estar vacía")
        if not self.id_especialidad or not str(self.id_especialidad).strip():
            raise ValueError("La especialidad del doctor no puede estar vacía")

    def registrar_doctor(self, doctores):
        self.validar_datos()
        doctores[self.id_doctor] = self.to_dict()
        return doctores

    def to_dict(self):
        return {
            "id_doctor": self.id_doctor,
            "nombre": self.nombre,
            "jvpo_doctor": self.jvpo_doctor,
            "id_sucursal": self.id_sucursal,
            "id_especialidad": self.id_especialidad
        }

    def __str__(self):
        return f"Doctor({self.id_doctor}, {self.nombre}, especialidad={self.id_especialidad})"
