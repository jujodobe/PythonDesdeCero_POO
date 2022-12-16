import sqlite3
from Cuentas.DAO.DAO_Cuentas import DAO_Cuenta
from Cuentas.Models.Cuenta import Cuenta

conexion = sqlite3.connect('DAO/cuenta.db')

CREAR_TABLA_USUARIO = '''
    CREATE TABLE IF NOT EXISTS usuario(
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "nombre" TEXT NOT NULL UNIQUE,
        "clave" TEXT NOT NULL);
        '''

crear_tabla_cuenta = ''' 
    CREATE TABLE IF NOT EXISTS cuenta(
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "numero"	TEXT NOT NULL,
        "titular"	TEXT NOT NULL,
        "saldo"	INTEGER NOT NULL,
        "limiteSaldo"	INTEGER NOT NULL,
        "usuario_id" INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuario (id)
    );'''



cursor = conexion.cursor()
cursor.execute(CREAR_TABLA_USUARIO)
cursor.execute(crear_tabla_cuenta)
cursor.close()

def ejecutar():
    daoCuenta = DAO_Cuenta(conexion)
    opcion = int(input('''Operaciones realizar
    1- Insertar 
    2- Modificar 
    3- Eliminar 
    4- Consultar Registro 
    5- Listar Registros
    Ingrese la opcion: '''))



    if opcion == 1:
        cuenta = inicializarNuevaCuenta()
        cuentaGuardada = daoCuenta.guardar(cuenta)
        print(cuentaGuardada.getId())










def inicializarNuevaCuenta():
    numero = input("Ingrese el número de cuenta: ")
    titular = input("Ingrese el titular de la cuenta: ")
    saldo = int(input("Ingrese el saldo de la cuenta"))
    limiteSaldo = int(input("Ingrese el límite del saldo"))
    return Cuenta(0, numero, titular, saldo, limiteSaldo)


# print(modificarDatos("112233", "Julio Miranda", 500000, 2000000, 4))
ejecutar()