import tkinter as tk
import sys
import os

# Agrega la carpeta raíz del proyecto al inicio de la búsqueda de módulos.
# Esto permite importar archivos del proyecto aunque cambie el lugar desde
# donde se ejecute el programa.
sys.path.insert(0, os.path.dirname(__file__))

from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppTkinter


def main():
    # Se crea el servicio antes de la interfaz porque la interfaz lo usa
    # para registrar y consultar los vehículos.
    servicio = GarajeServicio()

    # Se crea la ventana principal de la aplicación.
    root = tk.Tk()

    # Se inicia la interfaz gráfica pasándole la ventana y el servicio.
    AppTkinter(root, servicio)

    # Mantiene la ventana abierta y esperando eventos del usuario.
    root.mainloop()


if __name__ == "__main__":
    main()