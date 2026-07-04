class Producto:
    """Clase padre que representa un producto general del restaurante"""

    def __init__(self, nombre: str, precio: float, disponibilidad: bool = True):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado (privado)
        self.disponibilidad = disponibilidad

        # Validación inicial
        if self.__precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")

    # Métodos para acceder y modificar el precio
    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"✅ Precio actualizado: {self.nombre} → ${nuevo_precio:.2f}")
        else:
            print("❌ El precio no puede ser cero ni negativo")

    # Método base
    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"Nombre: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"