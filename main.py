from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def menu():
    print("\n--- Restaurante App ---")
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Vender producto")
    print("4. Consultar ventas por usuario")
    print("5. Listar productos")
    print("6. Salir")

def main():
    restaurante = Restaurante()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            rol = input("Rol: ")  # tu clase Usuario requiere rol
            usuario = Usuario(identificacion, nombre, rol)
            restaurante.registrar_usuario(usuario)
            print("Usuario registrado correctamente.")

        elif opcion == "2":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            producto = Producto(codigo, nombre, categoria, precio, stock)
            restaurante.registrar_producto(producto)
            print("Producto registrado correctamente.")

        elif opcion == "3":
            identificacion = input("Identificación usuario: ")
            codigo = input("Código producto: ")
            cantidad = int(input("Cantidad: "))
            if restaurante.vender_producto(codigo, identificacion, cantidad):
                print("Venta registrada correctamente.")
            else:
                print("No se pudo realizar la venta.")

        elif opcion == "4":
            identificacion = input("Identificación usuario: ")
            ventas = restaurante.ventas_por_usuario(identificacion)
            if ventas:
                print("\n--- Ventas del usuario ---")
                for v in ventas:
                    producto = restaurante.buscar_producto(v.producto_codigo)
                    print(f"Producto: {producto.nombre}, Cantidad: {v.cantidad}")
            else:
                print("No hay ventas registradas para este usuario.")

        elif opcion == "5":
            restaurante.listar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
