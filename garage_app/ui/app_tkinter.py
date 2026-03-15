import tkinter as tk
from tkinter import messagebox
from servicios.garaje_servicio import GarajeServicio


class AppTkinter:
    """Interfaz gráfica de la aplicación de gestión de garaje."""

    def __init__(self, root: tk.Tk, servicio: GarajeServicio):
        # root representa la ventana principal creada en main.py.
        self.root = root

        # servicio contiene la lógica para registrar y listar vehículos.
        self.servicio = servicio

        self._configurar_ventana()
        self._crear_componentes()