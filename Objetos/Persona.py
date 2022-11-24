class Personas:

    def __init__(self):
        ...

    def __init__(self, nombre, apellido, edad):
        self.__Nombre = nombre
        self.__Apellido = apellido
        self.__Edad = edad

    def __int__(self, edad):
        self.__Edad = edad

    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getNombre(self):
        return self.__Nombre

    def setApellido(self, apellido):
        self.__Apellido = apellido

    def getApellido(self):
        return self.__Apellido

    def setEdad(self, edad):
        self.__Edad = edad

    def getEdad(self):
        return self.__Edad