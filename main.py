import customtkinter as ctk
from frame import GuiFrame


class Ventana(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Retailsys GUI")
        self.geometry("1100x650+120+10")
        self.resizable(False, False)
        
        self.gui = GuiFrame(self)
        self.gui.pack()