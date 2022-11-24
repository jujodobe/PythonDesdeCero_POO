# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.pi

from Objetos.Alumnos import Alumnos
from Objetos.Persona import Personas


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
def practicasAlumnos():

    alumnos = Alumnos("Maria", "Gonzalez", 20)
    alumnos.setNombre(input("Ingrese el nombre: "))
    alumnos.setApellido(input("Ingrese su apellido: "))
    alumnos.setEdad(input("Ingrese su edad: "))
    print(f"Bienvenido {alumnos.getNombre()} {alumnos.getApellido()}, usted tiene {alumnos.getEdad()}")

practicasAlumnos()