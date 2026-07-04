from modelos.producto import Producto

class Bebida(Producto):
    """Clase hija que representa una bebida, hereda de Producto"""

    def __init__(self, nombre: str, precio: float, volumen_ml: int, disponibilidad: bool = True):
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base} | Volumen: {self.volumen_ml} ml"