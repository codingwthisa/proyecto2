from claseProducto import Producto

class ControlPlagas(Producto):
    def __init__(self, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__("Control de Plagas", nombre, frecuencia_aplicacion, valor, periodo_carencia)
        self.periodo_carencia = periodo_carencia

    def calcular_precio(self):
        precio_final = self.valor
        if self.periodo_carencia > 30:
            precio_final *= 1.05  # aumenta el 5% si el periodo de carencia es mayor a 30 días
        return precio_final


