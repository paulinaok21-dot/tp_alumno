
class Alumno:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.notas = []

    def getInfo(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Curso: ", self.curso)

    def getNotas(self):
        cont = 1
        for nota in self.notas:
            print(cont, " - ", nota)
            cont += 1

    def setNota(self, nota):
        if nota > 0 and nota <= 10:
            print("NOTA GUARDADA")
            self.notas.append(nota)
        else:
            print("NOTA NO VALIDA")

    def setNombre(self, nombre):
        self.nombre = nombre
