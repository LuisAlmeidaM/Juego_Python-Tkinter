import tkinter as tk

"""
Clase que define la estructura principal de la 
ventana de la aplicacion.
"""
class Ventana(tk.Tk):
    def __init__(self, anchoVentana, altoVentana, fps=60):
        # Llama al constructor de la clase base (tk.Tk)
        super().__init__()  

        # == Configuracion de la ventana ==
        self.title("Ventana")               # Titulo de la ventana
        self.anchoVentana = anchoVentana    # Ancho de la ventana
        self.altoVentana = altoVentana      # Alto de la ventana
        self.FPS = fps
        self.intervalo_ms = int (1000/self.FPS)

        # Centrar la ventana
        self.CentrarVentana()

        # Creación del canvas
        self.CrearCanvas()

        # Iniciar bucle de juego
        self.BucleDeJuego()

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
    
    def CrearCanvas(self):
        # 1. Crear el objeto canvas
        self.canvas = tk.Canvas(self, bg="green")

        # 2. Posicionar el canvas en la ventana
        self.canvas.pack(fill="both", expand=True)

    def BucleDeJuego(self):
        """
        Funcion principal que simula el bucle de juego
        Llama la logica de actualizacion y luego se programa para la proxima
        llamada
        """
        # 1. Logica del juego (actualizacion de Estado)
        self.actualizarJuego()
        # 2. Proogramación de la siguienteactualizacion
        self.after(self.intervalo_ms, self.BucleDeJuego)
    
    def actualizarJuego(self):
        print(f"FPS: {self.FPS} - Ticks: {self.winfo_name()}")

# Ejecución principal del programa
if __name__== "__main__":
    juego = Ventana(640, 480)                   # Objeto juego
    juego.mainloop()                            # Ejecución del juego
