from articulo import Articulo
from linea import Linea
class Factura:
    __ultima = 0
    def __init__(self, cliente):
        Factura.__ultima += 1
        self.__set_numero(Factura.__ultima)
        self.__set_cliente(cliente)
        self.__lineas = []

    def __str__(self):
        return f'Factura Nº{self.numero()} - {self.cliente()}'

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

    def __esta_articulo(self, articulo):
        for linea in self.__get_lineas():
            if linea.articulo() == articulo:
                return True
        return False

    def agregar_articulo(self, articulo: Articulo, cantidad):
        """No puede haber dos lineas del mismo articulo."""
        try:
            linea = self.__buscar_linea(articulo)
            cantidad_original = linea.cantidad()
            self.__eliminar_linea(linea)
        except ValueError:
            cantidad_original = 0
        linea = Linea(articulo, cantidad_original + cantidad)
        self.__agregar_linea(linea)

    def reducir_articulo(self, articulo: Articulo, cantidad = 1):
        self.agregar_articulo(articulo, - cantidad)

    def quitar_articulo(self, articulo: Articulo):
        self.__eliminar_linea(self.__buscar_linea(articulo))

    def __imprimir_lineas(self):
        for linea in self.__get_lineas():
            print(linea)

    def __total(self):
        total = 0
        for linea in self.__get_lineas():
            total += linea.articulo().precio() * linea.cantidad()
        return total

    def imprimir_factura(self):
        """Imprime por la salida la factura."""
        print(self)
        print()
        print('| Artículo | P.u. | Cantidad | Subtotal |')
        print()
        self.__imprimir_lineas()
        print()
        print(f'| Total: {self.__total()}€ |')
