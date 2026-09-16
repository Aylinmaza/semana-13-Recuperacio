class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def to_dict(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(data: dict) -> "Venta":
        return Venta(
            usuario_id=data["usuario_id"],
            producto_codigo=data["producto_codigo"],
            cantidad=data["cantidad"]
        )