from Cuentas.Models.usuario import Usuario


class DAO_Usuario:

    def __init__(self, conexionDB):
        self.__conexionDB = conexionDB

    def consultarUsuarioPorId(self, id):
        cursor = self.__conexionDB.cursor()
        cursor.execute(f"SELECT * FROM usuario")
        tupla = cursor.fetchone()
        usuario = Usuario(tupla[0], tupla[1], tupla[2])
        return usuario