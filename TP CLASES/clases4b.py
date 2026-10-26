
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

    def getNombre(self):
        return self.nombre

    def getNotas(self):
        cont = 1
        for nota in self.notas:
            print(cont, " - ", nota)
            cont += 1

    def setNota(self, nota):
        if nota > 0 and nota <= 10:
            self.notas.append(nota)
            print("Nota cargada")
        else:
            print("Nota invalida")

    def setEdad(self, nuevaEdad):
        self.edad = nuevaEdad
