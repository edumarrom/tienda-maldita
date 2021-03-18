class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.__set_dni(dni)
        self.__set_nombre(nombre)
        self.__set_apellidos(apellidos)

        def dni(self):
            return self.__dni

        def nombre(self):
            return self.__nombre

        def apellidos(self):
            return self.__apellidos

        def __set_dni(self, dni):
            self.__dni = dni

        def __set_nombre(self, nombre):
            self.__nombre = nombre

        def __set_apellidos(self, apellidos):
            self.__apellidos = apellidos
