# Restaurante App - Semana 6 | Programación Orientada a Objetos

**Nombre del estudiante:** Erikg Abad

---

## 📝 Descripción del sistema
Esta aplicación es un sistema sencillo desarrollado en Python para administrar los productos del menú de un restaurante. Su objetivo es aplicar y demostrar los principios fundamentales de la Programación Orientada a Objetos: **herencia, encapsulación y polimorfismo**, siguiendo una estructura modular organizada para facilitar su comprensión y mantenimiento.

---

## 🗂️ Estructura del proyecto
El proyecto se organiza en carpetas y archivos con responsabilidades claras:

restaurante_app_S_6/

├── modelos/

│ ├── init.py # Marca la carpeta como módulo de Python

│ ├── producto.py # Clase padre con atributos y métodos comunes

│ ├── platillo.py # Clase hija que representa platos de comida

│ └── bebida.py # Clase hija que representa bebidas

├── servicios/

│ ├── init.py # Marca la carpeta como módulo de Python

│ └── restaurante.py # Clase encargada de gestionar el listado de productos

├── main.py # Archivo principal, punto de inicio del programa

└── README.md # Documentación del proyecto


---

## 🔗 Relación de herencia aplicada
Se crea una jerarquía lógica de clases:
- **`Producto`**: Es la clase base o padre, contiene los atributos comunes a todos los productos: `nombre`, `precio` y `disponibilidad`.
- **`Platillo`**: Hereda todos los atributos y métodos de `Producto`, y agrega su propio atributo: `tiempo_preparacion`.
- **`Bebida`**: También hereda de `Producto`, y agrega su atributo propio: `volumen_ml`.

Se utiliza la función `super()` para reutilizar el código de la clase padre sin duplicarlo.

---

## 🔒 Aplicación de encapsulación
Se protege el atributo **`__precio`** definiéndolo como privado (con doble guion bajo), de modo que no se puede modificar directamente desde fuera de la clase. Para acceder y cambiar su valor de forma controlada se usan:
- `obtener_precio()`: Devuelve el valor actual del precio.
- `cambiar_precio()`: Permite modificar el precio, incluyendo una validación que impide ingresar valores negativos o iguales a cero.

---

## 🔄 Aplicación de polimorfismo
Se demuestra este principio mediante el método `mostrar_informacion()`, que se define en la clase padre y se **sobrescribe** en cada clase hija:
- En `Platillo`: Muestra además el tiempo de preparación.
- En `Bebida`: Muestra además el volumen en mililitros.

Al recorrer la lista de productos, el mismo método se ejecuta con resultados diferentes según el tipo de objeto.

---

## 💡 Reflexión sobre la POO
Aplicar la Programación Orientada a Objetos y organizar el código en módulos permite desarrollar sistemas más ordenados, reutilizables y fáciles de mantener. La herencia evita duplicar código, la encapsulación protege la integridad de los datos y el polimorfismo da flexibilidad para ampliar funcionalidades sin modificar gran parte del código existente. Esto hace que el proyecto sea más escalable y fácil de corregir o actualizar en el futuro.

---

## 🚀 Ejecución del programa
Para iniciar la aplicación, ejecute desde la carpeta raíz del proyecto:
```bash
python main.py

============================================================
👋 Bienvenido al sistema del Restaurante - Desarrollado por: Erikg Abad
============================================================

📦 Producto agregado: Lasaña de carne
📦 Producto agregado: Ensalada fresca
📦 Producto agregado: Jugo de naranja natural
📦 Producto agregado: Café americano

--- Actualización de precios ---
✅ Precio actualizado: Lasaña de carne → $13.00
❌ El precio no puede ser cero ni negativo

==================================================
📋 MENÚ DEL RESTAURANTE: SABOR CASERO
==================================================
- Nombre: Lasaña de carne | Precio: $13.00 | Estado: Disponible | Tiempo de preparación: 25 min
- Nombre: Ensalada fresca | Precio: $6.75 | Estado: No disponible | Tiempo de preparación: 10 min
- Nombre: Jugo de naranja natural | Precio: $3.20 | Estado: Disponible | Volumen: 350 ml
- Nombre: Café americano | Precio: $2.10 | Estado: Disponible | Volumen: 200 ml
==================================================
