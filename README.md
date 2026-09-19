# Restaurante App
##  para el ingreso de la interfaz grafica se utilizara como usuario la identificacion 
## 🎯 Propósito
Esta aplicación simula el sistema de un restaurante utilizando **Python** y **Tkinter**.  
Permite gestionar el acceso de usuarios, visualizar productos registrados y mostrar la interfaz principal del sistema.  
La funcionalidad de **Ventas** está identificada como pendiente para futuras versiones.

---

## 📂 Estructura de carpetas y archivos
restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   └── usuarios.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── usuario.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   └── main.py
└── README.md
---

## 🔄 Flujo de la aplicación
1. Se ejecuta `main.py`.
2. Se muestra la **LoginView** (usuario y contraseña).
3. El **RestauranteServicio** valida las credenciales.
4. Si son correctas → se carga la **MainView**.
5. En la **MainView** se pueden consultar:
   - Usuarios registrados.
   - Productos registrados.
   - Ventas (pendiente).
6. Al cerrar sesión → se regresa a la **LoginView** en la misma ventana.

---

## 🖥️ Vistas implementadas
- **LoginView**: formulario de acceso con validación de credenciales.
- **MainView**: panel principal con opciones de usuarios y productos.
- **Ventas**: identificada como funcionalidad pendiente.

---

## ▶️ Pasos para ejecutar
1. Clonar o descargar el repositorio.  
2. Verificar que Python esté instalado (`python --version`).  
3. Ubicarse en la carpeta del proyecto:  
   ```bash
   cd Restaurante