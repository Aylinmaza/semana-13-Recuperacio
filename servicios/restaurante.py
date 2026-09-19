from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        servicio = ArchivoServicio()
        self.productos = servicio.cargar("productos", Producto)
        self.usuarios = servicio.cargar("usuarios", Usuario)
        self.servicio = servicio

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

    def validar_acceso(self, usuario, password):
        for u in self.usuarios:
            if u.identificacion == usuario and u.password == password:
                return True
        return False

