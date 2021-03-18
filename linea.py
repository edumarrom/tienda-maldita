class Linea:
    def __init__(self, articulo, cantidad):
        self.__set_articulo(articulo)
        self.__set_cantidad(cantidad)

        def articulo(self):
            return self.__articulo

        def cantidad(self):
            return self.__cantidad

        def __set_articulo(self, articulo):
            self.__articulo = articulo

        def __set_cantidad(self, cantidad):
            self.__cantidad = cantidad
