class Usuario:

    def __init__(self, id = 0, nombre = "", clave = ""):
        self.__id = id
        self.__nombre = nombre
        self.__clave = clave

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getClave(self):
        return self.__clave

    def setClave(self, clave):
        self.__clave = clave