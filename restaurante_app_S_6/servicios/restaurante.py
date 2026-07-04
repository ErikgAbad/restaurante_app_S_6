class Restaurante:
    """Clase de servicio para administrar los productos"""

    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"📦 Agregado: {producto.nombre}")

    def mostrar_menu(self):
        print("\n" + "="*50)
        print(f"📋 MENÚ: {self.nombre_restaurante.upper()}")
        print("="*50)
        if not self.lista_productos:
            print("Sin productos registrados")
            return
        for p in self.lista_productos:
            print(f"- {p.mostrar_informacion()}")
        print("="*50)