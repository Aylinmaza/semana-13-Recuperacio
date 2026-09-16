from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self) -> None:
        self._archivo = ArchivoServicio()
        self.productos: list[Producto] = self._archivo.cargar("productos", Producto)
        self.usuarios: list[Usuario] = self._archivo.cargar("usuarios", Usuario)
        self.ventas: list[Venta] = self._archivo.cargar("ventas", Venta)

        self.info_sistema: tuple = ("RestauranteApp", "Versión 11.0")
        self.config: dict = {"modo": "interactivo", "max_productos": 100}

        # Índices auxiliares
        self.productos_por_codigo: dict[str, Producto] = {p.codigo: p for p in self.productos}
        self.usuarios_por_id: dict[str, Usuario] = {u.identificacion: u for u in self.usuarios}
        self.ventas_por_usuario_dict: dict[str, list[Venta]] = {}
        for v in self.ventas:
            self.ventas_por_usuario_dict.setdefault(v.usuario_id, []).append(v)

        # Set para categorías únicas
        self.categorias_unicas: set = {p.categoria for p in self.productos}

    # ---------------------------
    # Gestión de productos
    # ---------------------------
    def registrar_producto(self, producto: Producto):
        if producto.codigo in self.productos_por_codigo:
            raise ValueError("El código ya existe.")
        self.productos.append(producto)
        self.productos_por_codigo[producto.codigo] = producto
        self.categorias_unicas.add(producto.categoria)
        self._archivo.guardar("productos", self.productos)

    def buscar_producto(self, codigo: str):
        return self.productos_por_codigo.get(codigo)

    def eliminar_producto(self, codigo: str):
        producto = self.productos_por_codigo.pop(codigo, None)
        if producto:
            self.productos.remove(producto)
            self._archivo.guardar("productos", self.productos)

    # ---------------------------
    # Gestión de usuarios
    # ---------------------------
    def registrar_usuario(self, usuario: Usuario):
        if usuario.identificacion in self.usuarios_por_id:
            raise ValueError("La identificación ya existe.")
        self.usuarios.append(usuario)
        self.usuarios_por_id[usuario.identificacion] = usuario
        self._archivo.guardar("usuarios", self.usuarios)

    def buscar_usuario(self, identificacion: str):
        return self.usuarios_por_id.get(identificacion)

    def eliminar_usuario(self, identificacion: str):
        usuario = self.usuarios_por_id.pop(identificacion, None)
        if usuario:
            self.usuarios.remove(usuario)
            self._archivo.guardar("usuarios", self.usuarios)

    # ---------------------------
    # Gestión de ventas
    # ---------------------------
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            print("Error: usuario o producto no existe.")
            return False
        if cantidad <= 0 or producto.stock < cantidad:
            print("Error: cantidad inválida o stock insuficiente.")
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self.ventas.append(venta)
        self.ventas_por_usuario_dict.setdefault(usuario.identificacion, []).append(venta)
        producto.vender(cantidad)

        self._archivo.guardar("ventas", self.ventas)
        self._archivo.guardar("productos", self.productos)
        return True

    def ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        return self.ventas_por_usuario_dict.get(identificacion_usuario, [])

    def listar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            print("\n--- Lista de productos ---")
            for producto in self.productos:
                print(producto)
