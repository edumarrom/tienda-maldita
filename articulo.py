class Articulo:
    def __init__(self, codigo, denominacion, precio):
        self.__set_codigo(codigo)
        self.__set_denominacion(denominacion)
        self.__set_precio(precio)

    def codigo(self):
        return self.__codigo

    def denominacion(self):
        return self.__denominacion

    def precio(self):
        return self.__precio

    def __set_codigo(self, codigo):
        self.__codigo = codigo

    def __set_denominacion(self, denominacion):
        self.__denominacion = denominacion

    def __set_precio(self, precio):
        self.__precio = precio
