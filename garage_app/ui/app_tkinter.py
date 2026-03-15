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

# Métodos privados para configurar la ventana y crear los componentes de la interfaz.

    def _configurar_ventana(self):
        """Configura la ventana principal."""
        self.root.title("Sistema Básico de Gestión de Garaje")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

    def _crear_componentes(self):
        """Crea los elementos visuales de la interfaz."""
        # Título principal de la aplicación.
        titulo = tk.Label(
            self.root,
            text="Sistema Básico de Gestión de Garaje",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        # Este marco agrupa las etiquetas y cajas de texto del formulario.
        marco_formulario = tk.Frame(self.root)
        marco_formulario.pack(pady=10)

        # Estas variables permiten leer y limpiar fácilmente el contenido
        # de cada campo de entrada.
        self.variable_placa = tk.StringVar()
        self.variable_marca = tk.StringVar()
        self.variable_propietario = tk.StringVar()

        etiqueta_placa = tk.Label(marco_formulario, text="Placa:")
        etiqueta_placa.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entrada_placa = tk.Entry(
            marco_formulario,
            textvariable=self.variable_placa
        )
        self.entrada_placa.grid(row=0, column=1, padx=5, pady=5)

        etiqueta_marca = tk.Label(marco_formulario, text="Marca:")
        etiqueta_marca.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.entrada_marca = tk.Entry(
            marco_formulario,
            textvariable=self.variable_marca
        )
        self.entrada_marca.grid(row=1, column=1, padx=5, pady=5)

        etiqueta_propietario = tk.Label(marco_formulario, text="Propietario:")
        etiqueta_propietario.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.entrada_propietario = tk.Entry(
            marco_formulario,
            textvariable=self.variable_propietario
        )
        self.entrada_propietario.grid(row=2, column=1, padx=5, pady=5)

        # Este marco organiza los botones del formulario.
        marco_botones = tk.Frame(self.root)
        marco_botones.pack(pady=10)

        boton_agregar = tk.Button(
            marco_botones,
            text="Agregar vehículo",
            command=self._agregar_vehiculo
        )
        boton_agregar.grid(row=0, column=0, padx=10)

        boton_limpiar = tk.Button(
            marco_botones,
            text="Limpiar",
            command=self._limpiar_campos
        )
        boton_limpiar.grid(row=0, column=1, padx=10)

        # Etiqueta que indica la sección donde se mostrarán los registros.
        etiqueta_lista = tk.Label(
            self.root,
            text="Vehículos registrados:",
            font=("Arial", 11, "bold")
        )
        etiqueta_lista.pack(pady=(10, 5))

        # Este marco contiene la lista y su barra de desplazamiento.
        marco_lista = tk.Frame(self.root)
        marco_lista.pack(pady=5)

        self.lista_vehiculos = tk.Listbox(marco_lista, width=55, height=10)
        self.lista_vehiculos.pack(side="left", padx=(0, 5))

        barra_desplazamiento = tk.Scrollbar(marco_lista, orient="vertical")
        barra_desplazamiento.pack(side="right", fill="y")

        # Se conecta la barra de desplazamiento con la lista.
        self.lista_vehiculos.config(yscrollcommand=barra_desplazamiento.set)
        barra_desplazamiento.config(command=self.lista_vehiculos.yview)

        # Esta etiqueta muestra cuántos vehículos hay registrados.
        self.etiqueta_total = tk.Label(self.root, text="Total de vehículos: 0")
        self.etiqueta_total.pack(pady=10)