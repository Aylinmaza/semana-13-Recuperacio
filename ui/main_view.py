import tkinter as tk
from tkinter import messagebox

class MainView(tk.Frame):
    def __init__(self, master, servicio, on_logout):
        super().__init__(master)
        self.servicio = servicio
        self.on_logout = on_logout

        # Título
        tk.Label(self, text="Panel Principal - Restaurante", font=("Arial", 14, "bold")).pack(pady=10)

        # Botones de funcionalidades actuales
        tk.Button(self, text="Usuarios", command=self.mostrar_usuarios).pack(pady=5)
        tk.Button(self, text="Productos", command=self.mostrar_productos).pack(pady=5)

        # Funcionalidad futura (identificada pero no implementada)
        tk.Button(self, text="Ventas (pendiente)", command=self.mostrar_mensaje).pack(pady=5)

        # Botón de cerrar sesión
        tk.Button(self, text="Cerrar sesión", command=self.on_logout).pack(pady=20)

        # Área de texto para mostrar resultados
        self.text_area = tk.Text(self, height=12, width=60)
        self.text_area.pack(pady=10)

    def mostrar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, "=== Lista de Usuarios ===\n")
        if not usuarios:
            self.text_area.insert(tk.END, "No hay usuarios registrados.\n")
        else:
            for u in usuarios:
                self.text_area.insert(tk.END, f"{u.nombre} ({u.identificacion}) - Rol: {u.rol}\n")

    def mostrar_productos(self):
        productos = self.servicio.listar_productos()
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, "=== Inventario de Productos ===\n")
        if not productos:
            self.text_area.insert(tk.END, "No hay productos registrados.\n")
        else:
            for p in productos:
                self.text_area.insert(tk.END, f"{p.nombre} - Stock: {p.stock}\n")

    def mostrar_mensaje(self):
        messagebox.showinfo("Ventas", "Funcionalidad en desarrollo")
