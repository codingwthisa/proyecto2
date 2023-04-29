class Producto:
    def __init__(self, tipo, registro_ICA, nombre, frecuencia_aplicacion, valor):
        self.tipo = tipo
        self.registro_ICA = registro_ICA
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor

    def calcular_precio(self):
        return self.valor

