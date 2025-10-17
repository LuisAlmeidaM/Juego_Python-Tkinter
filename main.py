import tkinter as tk

"""
Clase que define la estructura principal de la 
ventana de la aplicacion.
"""
class Ventana(tk.Tk):
    def __init__(self, anchoVentana, altoVentana):
        # Llama al constructor de la clase base (tk.Tk)
        super().__init__()  

        # == Configuracion minima de la ventana ==
        self.title("Ventana")               # Titulo de la ventana
        self.anchoVentana = anchoVentana    # Ancho de la ventana
        self.altoVentana = altoVentana      # Alto de la ventana

        # Centrar la ventana
        self.CentrarVentana()
    
    def CentrarVentana(self):
        """
        Calcula la posición para que la ventana aparezca en el centro de la pantalla 
        y aplica la geometría
        """
        # 1. Obtener el ancho y alto de la pantalla
        anchoPantalla = self.winfo_screenwidth()
        altoPantalla = self.winfo_screenheight()

        # 2. Calcular las coordenadas x,y para centrar la ventana
        posicionX = int((anchoPantalla / 2) - (self.anchoVentana / 2))
        posicionY = int((altoPantalla / 2) - (self.altoVentana / 2))

        # 3. Aplicar la Geometría
        self.geometry(f"{self.anchoVentana}x{self.altoVentana}+{posicionX}+{posicionY}")


# Ejecución principal del programa
if __name__== "__main__":
    juego = Ventana(640, 480)                   # Objeto juego
    juego.mainloop()                            # Ejecución del juego
