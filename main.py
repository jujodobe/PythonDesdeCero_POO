# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.pi

from Cuentas.Models.Cuenta import Cuenta

cuenta1 = Cuenta("123456", "Juan Perez", 100000, 1000000)
cuenta2 = Cuenta("456789", "Maria Gomez", 50000, 2000000)

continuidad = 1

while continuidad == 1:
    operacion = int(input("Que operacion desea realizar? \n 1- Deposito \n 2- retiro \n 3- Extracto \n Ingrese el Valor: "))
    if operacion == 1:
        cuenta1.deposita(int(input("Ingrese la cantidad a depositar: ")))

    if operacion == 2:
        cuenta1.retiro(int(input("Ingrese la cantidad a depositar: ")))

    if operacion == 3:
        cuenta1.extracto()

    continuidad = int(input("Desea continuar con las operaciones? \n 1 Afirmativo \n 2- Negativo \n Ingrese valor: "))




"""
print("\n DATOS DE LA CUENTA 1")
cuenta1 = Cuenta("123456", "Juan Perez", 100000, 1000000)

print("\n")
cuenta1.extracto()
cuenta1.deposita(int(input("ingrese la cantidad a depositar: ")))
print("\n")
cuenta1.extracto()
print("\n")
cuenta1.retiro(int(input("ingrese la cantidad a retirar: ")))
cuenta1.extracto()


print("\n DATOS DE LA CUENTA 2")

cuenta2 = Cuenta("456789", "Maria Gomez", 50000, 2000000)
print("\n")
cuenta2.extracto()
cuenta2.deposita(int(input("ingrese la cantidad a depositar: ")))
print("\n")
cuenta2.extracto()
print("\n")
cuenta2.retiro(int(input("ingrese la cantidad a retirar: ")))
print("\n")
cuenta2.extracto()
"""

"""
RELACION ENTRE CLASES

pais1 = Pais("Paraguay", "Marito")
print(pais1)

ciudad1 = Ciudad("Asuncion", 250000, pais1)
print(ciudad1)
"""



""" Prácticas con Personas """
#jorge = Personas("Juan", "Gomez", 30)
#Mario = Personas("Mario", "Gonzalez", 22)
#juan = Personas()


#def imprimir():
    #print(f"El nombre es: {jorge.getNombre()}")
    #jorge.setNombre(input("Ingrese el nombre"))
    #print(f"El nombre modificado es: {jorge.getNombre()}")

# imprimir()






""" Prácticas con Alumnos """
"""def practicasAlumnos():

    alumnos = Alumnos("Maria", "Gonzalez", 20)
    alumnos.setNombre(input("Ingrese el nombre: "))
    alumnos.setApellido(input("Ingrese su apellido: "))
    alumnos.setEdad(input("Ingrese su edad: "))
    print(f"Bienvenido {alumnos.getNombre()} {alumnos.getApellido()}, usted tiene {alumnos.getEdad()}")

practicasAlumnos()"""