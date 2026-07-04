from modelos.producto import Producto

class Platillo(Producto):
    """Clase hija que representa un platillo, hereda de Producto"""

    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int, disponibilidad: bool = True):
        # Reutilizamos constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.tiempo_preparacion = tiempo_preparacion

    # Sobreescritura para polimorfismo
    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tiempo de preparación: {self.tiempo_preparacion} min"