from clases import *
from clases4b import *
import clases
import clases4b

def menu():
    print("1-alumno de clases")
    print("2-alumno de clases4b")
    print("3-salir")
    op = int(input("Ingrese la opcion que desee elegir: "))
    return op

while True:
    op = menu()

    if op == 1:
        estudiante1 = clases.Alumno("nombre", 16, "4B")
        print("ALUMNO DE CLASES")
        estudiante1.getInfo()
        estudiante1.setNota(8)
        estudiante1.setNota(9)
        estudiante1.getNotas()
        estudiante1.setNombre("nuevo nombre")
        estudiante1.getInfo()

    elif op == 2:
        estudiante2 = clases4b.Alumno("nombre", 18, "7")
        print("ALUMNO DE CLASES4B")
        estudiante2.getInfo()
        print("Nombre:", estudiante2.getNombre())
        estudiante2.setNota(7)
        estudiante2.setNota(10)
        estudiante2.getNotas()
        estudiante2.setEdad(19)
        estudiante2.getInfo()

    elif op == 3:
        break


