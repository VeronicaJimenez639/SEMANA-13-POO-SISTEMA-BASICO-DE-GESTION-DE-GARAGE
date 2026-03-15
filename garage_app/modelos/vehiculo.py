class Vehiculo:
    """Representa los datos de un vehículo del garaje."""

    def __init__(self, placa: str, marca: str, propietario: str):
        # Se usan las propiedades para guardar los datos ya limpios.
        self.placa = placa
        self.marca = marca
        self.propietario = propietario