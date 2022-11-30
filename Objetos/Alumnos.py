from Objetos.Persona import Personas

class Alumnos(Personas):

    def __init__(self, nombre = "", apellido = "", edad = 0):
        super().__init__(nombre, apellido, edad)

    def __init__(self, edad):
        super().__init__(edad)

    def setNumeroInscripcion(self, numeroInscripcion):
        self.NumeroInscripcion = numeroInscripcion