from Cuentas.DAO.DAO_Usuario import DAO_Usuario
from Cuentas.DAO.DAO_Cuentas import DAO_Cuenta
from Cuentas.Models.Cuenta import Cuenta
#from Cuentas.Models.usuario import Usuario
import sqlite3

conexion = sqlite3.connect("DAO/cuenta.db")

dao_usuario = DAO_Usuario(conexion)
dao_cuenta = DAO_Cuenta(conexion)
Models_Cuenta = Cuenta()
#Models_Usuario = Usuario()
def iniciar():
        usuario = dao_usuario.consultarUsuarioPorId(1)
        Models_Cuenta.setUsuario(usuario)
        Models_Cuenta.setNumero(input(f"Ingrese el numero de cuenta para el usuario {usuario.getNombre()}: "))
        Models_Cuenta.setTitular(input(f"Ingrese el titular para la cuenta {Models_Cuenta.getNumero()}: "))
        Models_Cuenta.setSaldo(int(input(f"Ingrese el saldo inicial para la cuenta {Models_Cuenta.getNumero()}: ")))
        Models_Cuenta.setLimite(int(input(f"Ingrese el limite del saldo para la cuenta {Models_Cuenta.getNumero()}: ")))
        dao_cuenta.guardar(Models_Cuenta)

iniciar()