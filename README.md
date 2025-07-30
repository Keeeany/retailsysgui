# RetailSys GUI

**RetailSys GUI** es una interfaz gráfica desarrollada con `customtkinter` que simula un sistema de gestión para puntos de venta (retail). Este proyecto está enfocado en ofrecer una **base visual y estructural** lista para que otros desarrolladores la personalicen y completen según sus necesidades específicas.

---

## 🎯 Objetivo

El objetivo de este proyecto es proporcionar una **plantilla de interfaz modular y moderna** para sistemas de gestión de ventas. Aunque **no está completamente funcional**, su diseño modular permite ahorrar tiempo en la construcción de GUIs complejas desde cero.

---

## 🧩 Características

- Interfaz moderna usando [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)
- Menú superior con acceso a módulos:
  - Inventario
  - Registros
  - Control de caja
  - Reporte de ventas
  - Configuración (interfaz solo)
- Arquitectura dividida en archivos para fácil mantenimiento
- Soporte para cambio de color de fondo (modo claro/oscuro básico)

---

## ⚠️ Importante

> **Este proyecto NO está terminado.**
>
> Su propósito es servir como **plantilla de interfaz visual** para que tú o tu equipo la **modifiquen, extiendan o integren con bases de datos reales** y funcionalidades específicas.

---

```bash
RetailSysGUI/
├── index.py                # Entry point
├── main.py                 # Main window
├── frame.py                # GUI layout
├── gui.py                  # View classes (Inventory, Records, etc.)
├── README.md               # Documentation
└── .gitignore              # Git ignored files


## 🚀 Cómo ejecutar

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/RetailSysGUI.git

2. Ejecuta index.py para correrlo:
  Ejecuta el archivo principal:
   ```bash
    python index.py
