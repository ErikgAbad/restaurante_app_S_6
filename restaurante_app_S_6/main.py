# Agrega ESTAS 2 líneas al inicio para arreglar el error de rutas
import sys
sys.path.append(".")

# Ahora sí tus importaciones funcionarán
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    mi_restaurante = Restaurante("Sabor Casero")

    try:
        lasaña = Platillo("Lasaña de carne", 12.50, 25)
        ensalada = Platillo("Ensalada fresca", 6.75, 10, disponibilidad=False)
        jugo = Bebida("Jugo de naranja", 3.20, 350)
        cafe = Bebida("Café americano", 2.10, 200)
    except ValueError as err:
        print(f"Error: {err}")
        return

    mi_restaurante.agregar_producto(lasaña)
    mi_restaurante.agregar_producto(ensalada)
    mi_restaurante.agregar_producto(jugo)
    mi_restaurante.agregar_producto(cafe)

    print("\n--- Actualización de precios ---")
    lasaña.cambiar_precio(13.00)
    cafe.cambiar_precio(-1.50)

    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()