from Cuentas.Models.Cuenta import Cuenta
from Cuentas.DAO.DAO_Usuario import DAO_Usuario

import sqlite3



class DAO_Cuenta:

    def __init__(self, conexionDB):
        self.__conexionDB = conexionDB

    def guardar(self, cuenta):

        SQL_ACTUALIZA_CUENTA = f'''UPDATE FROM cuenta 
                                            SET numero = ?,
                                            titular = ?,
                                            saldo = ?,
                                            limiteSaldo = ?, 
                                            usuario_id = ?
                                   WHERE id = {cuenta.getId()} '''

        SQL_INSERTA_CUENTA = f'''INSERT INTO cuenta(numero, titular, saldo, limiteSaldo, usuario_id) values(?, ?, ?, ?, ?)'''

        cursor = self.__conexionDB.cursor() # Abrir cursor para escribir sentencias SQL

        if(cuenta.getId() != 0):
            cursor.execute(SQL_ACTUALIZA_CUENTA, (cuenta.getNumero(),
                                                  cuenta.getTitular(),
                                                  cuenta.getSaldo(),
                                                  cuenta.getLimite(),
                                                  Cuenta.getUsuario().getId()))
        else:
            cursor.execute(SQL_INSERTA_CUENTA, (cuenta.getNumero(),
                                                cuenta.getTitular(),
                                                cuenta.getSaldo(),
                                                cuenta.getLimite(),
                                                cuenta.getUsuario().getId()))
            cuenta.setId(cursor.lastrowid)
        self.__conexionDB.commit()
        cursor.close()
        return cuenta

    def listar(self):
        cursor = self.__conexionDB.cursor()
        cursor.execute("select * from cuenta")
        cuentas = traduce_cuentas(cursor.fetchall())
        cursor.close()
        return cuentas

    def consultarPorId(self, id):
        cursor = self.__conexionDB.cursor()
        cursor.execute(f"select * from cuenta where id = {id}")
        tupla = cursor.fetchone()
        daoUsuario = DAO_Usuario()
        usuario = daoUsuario.consultarPorId(tupla[5])
        cursor.close()
        return Cuenta(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], usuario)


    def eliminar(self, id):
        cursor = self.__conexionDB.cursor()
        cursor.execute(f"DELETE FROM cuenta WHERE id = {id}")
        self.__conexionDB.commit()
        cursor.close()


def traduce_cuentas(cuentas):
    def crea_cuenta_con_tupla(tupla):
        return Cuenta(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
    return list(map(crea_cuenta_con_tupla, cuentas))