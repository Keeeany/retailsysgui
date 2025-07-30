import customtkinter as ctk
from gui import VistaInventario, VistaRegistro, VistaControlCaja, VistaReporteVentas, VistaConfiguracion

class GuiFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # GRID frame principal (self)
        self.grid_rowconfigure(0, weight=0)  
        self.grid_rowconfigure(1, weight=0)  
        self.grid_rowconfigure(2, weight=1)  
        self.grid_columnconfigure(0, weight=0) 
        self.grid_columnconfigure(1, weight=1) 
        
        self.pack(expand=True, fill="both")
        
        # --- Contenedor superior ---
        self.contenedor_superior = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#000000")
        self.contenedor_superior.grid(row=0, column=0, columnspan=2, sticky="nsew") 
        self.contenedor_superior.pack_propagate(False)
        
        # GRID contenedor superior
        self.contenedor_superior.grid_columnconfigure(0, weight=1) # Columna para INVENTARIO
        self.contenedor_superior.grid_columnconfigure(1, weight=1) # Columna para REGISTROS
        self.contenedor_superior.grid_columnconfigure(2, weight=1) # Columna para CONTROL DE CAJA
        self.contenedor_superior.grid_columnconfigure(3, weight=1) # Columna para REPORTE DE VENTAS
        self.contenedor_superior.grid_columnconfigure(4, weight=1) # Columna para el botón de relleno (ej. CONFIGURACIÓN)
        
        
        # --- Área de contenido principal (donde iría el resto de la interfaz) ---
        self.main_content_area = ctk.CTkFrame(self, fg_color="#333333") 
        self.main_content_area.grid(row=2, column=1, sticky="nsew") 
        
        self.labelprincipal = ctk.CTkLabel(
            self.main_content_area,
            text="""¡Bienvenido a RETAILSYS GUI!
            ¡Para comenzar dale click a los apartados de arriba!
            """,
            text_color="#FFFFFF",
            font=("Arial", 28, "bold"),
            height=500
            )
        self.labelprincipal.pack()
        
        
        # --- BARRA DIVISORIA HORIZONTAL --- #
        self.separator_horizontal = ctk.CTkFrame(
            self, 
            height=2,  
            fg_color="gray",
            corner_radius=0
        )
        self.separator_horizontal.grid(row=1, column=0, columnspan=2, sticky="ew") 
        
        
        # WIDGETS === BOTONES
        
        # --- INVENTARIO --- #
        self.inventario = ctk.CTkButton(
            master=self.contenedor_superior, 
            text="INVENTARIO",
            font=("Arial", 20, "bold"),
            corner_radius=0,
            border_width=1,
            border_color="#FFFFFF",
            height=60, 
            width=200, 
            fg_color="#335E8F",
            text_color="white",
            command=lambda: self.cargar_vista(VistaInventario)
        )
        self.inventario.grid(row=0, column=0, padx=0, pady=0, sticky="ew") 
        
        
        # --- REGISTRO --- #
        self.registro = ctk.CTkButton(
            master=self.contenedor_superior, 
            text="REGISTROS",
            font=("Arial", 20, "bold"),
            corner_radius=0,
            border_width=1,
            border_color="#FFFFFF",
            height=60, 
            width=200, 
            fg_color="#335E8F",
            text_color="white",
            command=lambda: self.cargar_vista(VistaRegistro)
        )
        self.registro.grid(row=0, column=1, padx=0, pady=0, sticky="ew") 
        
        
        # --- CONTROL DE CAJA --- #
        self.controlcaja = ctk.CTkButton(
            master=self.contenedor_superior, 
            text="CONTROL DE CAJA",
            font=("Arial", 20, "bold"),
            corner_radius=0,
            border_width=1,
            border_color="#FFFFFF",
            height=60,      
            width=200,
            fg_color="#335E8F",
            text_color="white",
            command=lambda: self.cargar_vista(VistaControlCaja)
        )
        self.controlcaja.grid(row=0, column=2, padx=0, pady=0, sticky="ew") 

        # --- REPORTE DE VENTAS --- #
        self.reporteventas = ctk.CTkButton(
            master=self.contenedor_superior, 
            text="REPORTE DE VENTAS",
            font=("Arial", 20, "bold"),
            corner_radius=0,
            border_width=1,
            border_color="#FFFFFF",
            height=60,      
            width=200, 
            fg_color="#335E8F",
            text_color="white",
            command=lambda: self.cargar_vista(VistaReporteVentas)
        )
        self.reporteventas.grid(row=0, column=3, padx=0, pady=0, sticky="ew") 



        # --- BOTÓN CONFIGURACION --- # 
        self.configuracion = ctk.CTkButton(
            master=self.contenedor_superior, 
            text="CONFIGURACIÓN",
            font=("Arial", 20, "bold"),
            corner_radius=0,
            border_width=1,
            border_color="#FFFFFF",
            height=60,      
            width=200, #
            fg_color="#335E8F",
            text_color="white",
            command=lambda: self.cargar_vista(VistaConfiguracion)
        )
        self.configuracion.grid(row=0, column=4, padx=0, pady=0, sticky="ew")
    
    def cargar_vista(self, VistaClase):
        for widget in self.main_content_area.winfo_children():
            widget.destroy()
            nueva_vista = VistaClase(self.main_content_area)
            nueva_vista.pack(fill="both", expand=True)