from articulo import Articulo
from linea import Linea
class Factura:
    def __init__(self, numero, cliente):
        self.__set_numero(numero)
        self.__set_cliente(cliente)
        self.__lineas = []

        def numero(self):
            return self.__numero

        def cliente(self):
            return self.__cliente

        def __get_lineas(self):
            return self.__lineas

        def __set_numero(self, numero):
            self.__numero = numero

        def __set_cliente(self, cliente):
            self.__cliente = cliente

        def __buscar_linea(self, articulo):
            for linea in self.__get_lineas():
                if linea.articulo() == articulo:
                    return linea
            raise ValueError('El artículo no está en el carrito')

        def __agregar_linea(self, linea):
            self.__get_lineas().append(linea)

        def __eliminar_linea(self, linea):
            self.__get_lineas().remove(linea)

        def agregar_articulo(self, articulo: Articulo, cantidad):
            """No puede haber dos lineas del mismo articulo."""
            try:
                linea = self.__buscar_linea(articulo)
                cantidad_original = linea.cantidad()
                cantidad = linea.cantidad()
                self.__eliminar_linea(linea)
            except ValueError:
                cantidad_original = 0
            linea = Linea(articulo, cantidad + cantidad_original)

        def __esta_articulo(self, articulo):
            for linea in self.__get_lineas():
                if linea.articulo() == articulo:
                    return True
            return False

        def reducir_articulo(self, articulo: Articulo, cantidad = 1):
            self.agregar_articulo(articulo, -1)

        def quitar_articulo(self, articulo: Articulo):
            self.__eliminar_linea(self.__buscar_linea(articulo))
