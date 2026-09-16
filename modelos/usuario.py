class Usuario:
    def __init__(self, identificacion: str, nombre: str, rol: str) -> None:
        if not identificacion or not nombre or not rol:
            raise ValueError("Todos los campos deben estar completos.")

        self.identificacion = identificacion
        self.nombre = nombre
        self.rol = rol

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data: dict) -> "Usuario":
        return Usuario(
            identificacion=data["identificacion"],
            nombre=data["nombre"],
            rol=data["rol"]
        )

    def __str__(self) -> str:
        return f"{self.nombre} ({self.rol})"