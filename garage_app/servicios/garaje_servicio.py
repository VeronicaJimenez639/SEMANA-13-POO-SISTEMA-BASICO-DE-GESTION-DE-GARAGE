from modelos.vehiculo import Vehiculo


class GarajeServicio:
    """Contiene la lógica del sistema de gestión de garaje."""

    def __init__(self):
        # La lista privada almacena todos los vehículos registrados.
        self._vehiculos = []

    def agregar_vehiculo(self, placa: str, marca: str, propietario: str):
        """Agrega un vehículo si los datos son válidos."""
        # Se limpian los textos antes de validarlos.
        placa = placa.strip()
        marca = marca.strip()
        propietario = propietario.strip()

        # Se valida que no existan campos vacíos.
        if not placa or not marca or not propietario:
            return False, "Todos los campos son obligatorios."

        # Se valida que la placa no esté repetida.
        if self._buscar_vehiculo_por_placa(placa):
            return False, "Ya existe un vehículo con esa placa."

        # Si los datos son correctos, se crea el vehículo y se guarda.
        vehiculo = Vehiculo(placa, marca, propietario)
        self._vehiculos.append(vehiculo)

        return True, "Vehículo registrado correctamente."

    def listar_vehiculos(self):
        """Devuelve la lista de vehículos registrados."""
        return self._vehiculos
    
    def total_vehiculos(self):
        """Devuelve la cantidad total de vehículos registrados."""
        return len(self._vehiculos)

    def _buscar_vehiculo_por_placa(self, placa: str):
        """Busca un vehículo por placa dentro de la lista."""
        placa_buscada = placa.strip().upper()

        for vehiculo in self._vehiculos:
            if vehiculo.placa == placa_buscada:
                return vehiculo

        return None