from Objetos.Persona import Personas

class Alumnos(Personas):

    def __init__(self, nombre = "", apellido = "", edad = 0):
        super().__init__(nombre, apellido, edad)

    def __int__(self, edad):
        super().__int__(edad)

    def setNumeroInscripcion(self, numeroInscripcion):
        self.NumeroInscripcion = numeroInscripcion