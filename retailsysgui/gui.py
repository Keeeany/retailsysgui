import customtkinter as ctk


# --- INVENTARIO --- #

class VistaInventario(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#333333")
        label = ctk.CTkLabel(self, text="Inventario cargado", font=("Arial", 24))
        label.pack(pady=50)





# --- REGISTROS --- #

class VistaRegistro(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#333333")
        label = ctk.CTkLabel(self, text="Registro cargado", font=("Arial", 24))
        label.pack(pady=50)




# --- CONTROL CAJAS --- #

class VistaControlCaja(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#333333")
        label = ctk.CTkLabel(self, text="Contro de Caja cargado", font=("Arial", 24))
        label.pack(pady=50)





# --- REPORTE VENTAS --- #

class VistaReporteVentas(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#333333")
        label = ctk.CTkLabel(self, text="Reporte de Ventas cargado", font=("Arial", 24))
        label.pack(pady=50)



# --- CONFIGURACION --- #

class VistaConfiguracion(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#333333")
        label = ctk.CTkLabel(self, text="Configuracion cargado", font=("Arial", 24))
        label.pack(pady=50)
