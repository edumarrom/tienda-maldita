class Articulo:
    __ultimo = 0
    def __init__(self, denom, precio):
        Articulo.__ultimo += 1
        self.__set_codigo(Articulo.__ultimo)
        self.__set_denom(denom)
        self.__set_precio(precio)

    def codigo(self):
        return self.__codigo

    def denom(self):
        return self.__denom

    def precio(self):
        return self.__precio

    def __set_codigo(self, codigo):
        self.__codigo = codigo

    def __set_denom(self, denom):
        self.__denom = denom

    def __set_precio(self, precio):
        self.__precio = precio
