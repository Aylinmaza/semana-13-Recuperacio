import os
import json
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    def __init__(self):
        # Carpeta donde se guardarán los archivos
        self.base_path = "datos"
        os.makedirs(self.base_path, exist_ok=True)

        # Definimos los nombres de los archivos JSON dentro de la carpeta datos
        self.archivos = {
            "productos": os.path.join(self.base_path, "productos.json"),
            "usuarios": os.path.join(self.base_path, "usuarios.json"),
            "ventas": os.path.join(self.base_path, "ventas.json")
        }

    # Guardar una colección en su archivo correspondiente
    def guardar(self, nombre: str, objetos: list):
        try:
            with open(self.archivos[nombre], "w", encoding="utf-8") as f:
                json.dump([obj.to_dict() for obj in objetos], f, ensure_ascii=False, indent=4)
        except PermissionError:
            print(f"Error: no tiene permisos para escribir en {self.archivos[nombre]}.")

    # Cargar una colección desde su archivo correspondiente
    def cargar(self, nombre: str, clase):
        try:
            with open(self.archivos[nombre], "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [clase.from_dict(d) for d in datos]
        except FileNotFoundError:
            # Si el archivo no existe, devolvemos lista vacía
            return []
        except json.JSONDecodeError:
            print(f"Error: el archivo {self.archivos[nombre]} contiene JSON inválido.")
            return []
        except PermissionError:
            print(f"Error: no tiene permisos para leer {self.archivos[nombre]}.")
            return []
