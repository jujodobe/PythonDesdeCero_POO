import sqlite3

conexion = sqlite3.connect('cuenta.db')

crear_tabla_cuenta = ''' 
    CREATE TABLE IF NOT EXISTS cuenta(
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "numero"	TEXT NOT NULL,
        "titular"	TEXT NOT NULL,
        "saldo"	INTEGER NOT NULL,
        "limiteSaldo"	INTEGER NOT NULL
    );'''

cursor = conexion.cursor()

cursor.execute(crear_tabla_cuenta)


def insertarDatos(numero, titular, saldo, limiteSaldo):
    insertar = f'''INSERT INTO cuenta(numero, titular, saldo, limiteSaldo) 
                               values('{numero}','{titular}',{saldo},{limiteSaldo})'''
    cursor.execute(insertar)
    conexion.commit()

def modificarDatos(numero, titular,saldo, limiteSaldo, id):
    modificar = f'''UPDATE cuenta 
                    SET numero='{numero}', 
                        titular='{titular}',
                        saldo={saldo},
                        limiteSaldo={limiteSaldo} 
                    WHERE id = {id}'''
    cursor.execute(modificar)
    conexion.commit()

def eliminarRegistro(id):
    cursor.execute(f"DELETE FROM cuenta WHERE id = {id}")
    conexion.commit()

def listarDatos():
    cursor.execute("SELECT * FROM cuenta")
    return cursor.fetchall()

def consultarRegistro(id):
    cursor.execute(f"SELECT * FROM cuenta WHERE id = {id}")
    return cursor.fetchone()


def ejecutar():
    opcion = int(input('''Operaciones realizar
    1- Insertar 
    2- Modificar 
    3- Eliminar 
    4- Consultar Registro 
    5- Listar Registros
    Ingrese la opcion: '''))

    if opcion == 1:
        insertarDatos("456123", "Mariano Gonzalez", 20000, 1000000)
    if opcion == 2:
        modificarDatos("789456", "Maria Gomez", 200000, 1000000)
    if opcion == 3:
        eliminarRegistro(3)
    if opcion == 4:
        print(consultarRegistro(3))
    if opcion == 5:
        print(listarDatos())

#print(modificarDatos("112233", "Julio Miranda", 500000, 2000000, 4))
ejecutar()