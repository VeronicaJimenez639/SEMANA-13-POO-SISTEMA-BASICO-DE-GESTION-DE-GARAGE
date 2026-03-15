class Vehiculo:
    """Representa los datos de un vehículo del garaje."""

    def __init__(self, placa: str, marca: str, propietario: str):
        # Se usan las propiedades para guardar los datos ya limpios.
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, value):
        # La placa se guarda sin espacios extra y en mayúsculas
        # para que todas tengan el mismo formato.
        self._placa = value.strip().upper()

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        # Se eliminan espacios innecesarios antes de guardar la marca.
        self._marca = value.strip()

    @property
    def propietario(self):
        return self._propietario

    @propietario.setter
    def propietario(self, value):
        # Se limpia el nombre del propietario antes de almacenarlo.
        self._propietario = value.strip()
