from modelos.vehiculo import Vehiculo


class GarajeServicio:
    """Contiene la lógica del sistema de gestión de garaje."""

    def __init__(self):
        # La lista privada almacena todos los vehículos registrados.
        self._vehiculos = []