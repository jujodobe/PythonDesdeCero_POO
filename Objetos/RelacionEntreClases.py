class Pais:

    def __init__(self, nombre, presidente):
        self.__Nombre = nombre
        self.__Presidente = presidente

    def __str__(self):
        text = "El presidente del Pais {0} es: {1}"
        return text.format(self.__Nombre, self.__Presidente)


class Ciudad:
    """
    Clase de ciudad que contiene los parametros de
    1- Nombre de ciudad
    2- Habitantes
    3- Objeto Pais instanciado de la clase pais
    """
    def __init__(self, ciudad, habitantes, pais):
        self.__Ciudad = ciudad
        self.__Habitantes = habitantes
        self.__Pais = pais

    def __str__(self):
        text = f"Ciudad: {self.__Ciudad} - Nº Habitantes: {self.__Habitantes} ({self.__Pais})"
        return text


