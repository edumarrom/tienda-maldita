Ejercicios de Programación orientada a objetos: Tienda
---
Programación — DAW - Ricardo Pérez López - IES Doñana - Curso 2020/2021
---

Diseñar y codificar un modelo orientado a objetos de una tienda online donde hay clientes, artículos y facturas. Para ello:

1. Crear la clase Cliente con los atributos __dni, __nombre y __apellidos.
2. Crear la clase Articulo con los atributos __codigo, __denominacion y __precio.
3. Crear la clase Factura con los atributos __numero, __cliente y __lineas.
    1. Cada línea de factura debe almacenar un artículo y una cantidad.
    2.  El total de la factura no se debe almacenar, sino que se debe calcular automáticamente sumando el precio de cada artículo multiplicado por la cantidad.
    3. Las líneas de una factura pertenecen a esa factura.
    4. Las líneas de una factura se pueden añadir o eliminar de una factura, pero no modifcar.
4. Crear un módulo _principal.py_ que use las clases anteriores para representar un modelo dinámico de objetos donde existe una factura del cliente Rosa González que ha comprado dos televisores de 399 € cada uno y una tarjeta gráfca de 239 €. Imprimir por pantalla todos los datos de la factura como si fuera una factura real, incluyendo el importe total de la misma.
