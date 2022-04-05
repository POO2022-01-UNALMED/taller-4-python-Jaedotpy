

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    def __init__(self, grupo="grupo predeterminado", asignaturas= [], estudiantes=None, grado = 12):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self._grado = grado

    def getGrupo(self):
        return self._grupo
    
    def getGrado(self):
        return self._grado

    def getLista(self):
        return self.listadoAlumnos

    def getNumeroAsignaturas(self):
        return len(self._asignaturas)

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if lista is None:
            self.listadoAlumnos = [alumno]
        else:
            lista.append(alumno)
            if self.listadoAlumnos is None:
                self.listadoAlumnos = lista
            else:
                self.listadoAlumnos  = self.listadoAlumnos + lista
    
    def asignarNombre(self, nombre):
        self._grupo = nombre
