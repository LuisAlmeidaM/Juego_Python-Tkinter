import tkinter as tk

"""
Clase que define la estructura principal de la 
ventana de la aplicacion.
"""
class Ventana(tk.Tk):
    def __init__(self):
        # Llama al constructor de la clase base (tk.Tk)
        super().__init__()  

        # == Configuracion minima de la ventana ==
        self.title("Ventana")
        self.geometry("640x480")
        self.resizable(False,False)


# Ejecución principal del programa
if __name__== "__main__":
    juego = Ventana()
    juego.mainloop()
