import sqlite3


conexion = sqlite3.connect('cuenta.db')

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