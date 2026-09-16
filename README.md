# RestauranteApp

Aplicación en Python para la gestión de un restaurante. Permite registrar usuarios y productos, realizar ventas y consultar información de manera interactiva desde la consola. Los datos se almacenan en archivos JSON y se optimizan las búsquedas mediante índices auxiliares en memoria.

## Mejoras realizadas

- **Colecciones principales**: se mantienen listas (`productos`, `usuarios`, `ventas`) para recorrer y persistir la información en JSON.
- **Índices auxiliares con diccionarios**:
  - `productos_por_codigo` para búsquedas rápidas de productos por código.
  - `usuarios_por_id` para búsquedas rápidas de usuarios por identificación.
  - `ventas_por_usuario_dict` para consultar ventas de un usuario sin recorrer toda la lista.
- **Uso de set**: `categorias_unicas` para obtener categorías únicas de productos.
- **Sincronización automática**: al registrar, modificar o eliminar datos se actualizan tanto las listas principales como los índices auxiliares.
- **Reconstrucción de índices**: al iniciar el programa se reconstruyen los diccionarios y sets a partir de los objetos cargados desde JSON.

## Organización del proyecto

- `modelos/`  
  - `Producto`: código, nombre, categoría, precio y stock.  
  - `Usuario`: identificación, nombre y rol.  
  - `Venta`: relación entre usuario y producto con cantidad.

- `servicios/`  
  - `ArchivoServicio`: manejo de persistencia en archivos JSON.  
  - `Restaurante`: lógica principal de gestión con índices auxiliares.

- `main.py`  
  Menú interactivo en consola para ejecutar las operaciones.

## Ejecución

1. Clonar o descargar el proyecto.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

   ```bash
   python main.py
## Pruebas principales realizadas
Registrar usuario: se añade un nuevo usuario y se guarda en usuarios.json.

Registrar producto: se añade un producto con código único y se guarda en productos.json.

Vender producto: se descuenta stock, se registra la venta en ventas.json y se actualiza el índice ventas_por_usuario_dict.
Consultar ventas por usuario: se muestran las ventas de un usuario directamente desde el índice auxiliar.

Listar productos: se imprime la lista completa de productos registrados.

Categorías únicas: se obtiene el conjunto de categorías registradas en el sistema.