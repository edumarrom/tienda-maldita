class Linea:
    def __init__(self, articulo, cantidad):
        self.__set_articulo(articulo)
        self.__set_cantidad(cantidad)

    def __str__(self):
        return f'| {self.articulo().denom()} | {self.articulo().precio()}€ | {self.__cantidad} | {self.subtotal()}€ |'

    def articulo(self):
        return self.__articulo

    def cantidad(self):
        return self.__cantidad

    def __set_articulo(self, articulo):
        self.__articulo = articulo

    def __set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def subtotal(self):
        """Devuelve el subtotal de la línea, a partir del precio del artículo y la cantidad del mismo."""
        return self.articulo().precio() * self.cantidad()
