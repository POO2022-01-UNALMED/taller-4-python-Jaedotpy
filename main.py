from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

if __name__ == "__main__":
    asignatura1 = Asignatura("Matematicas")
    asignatura2 = Asignatura("Castellano", "Salon 201")
    grupo1 = Grupo()

    print(asignatura1.getNombre())
    print("Grupo de estudiantes: " + grupo1.getGrupo())
    print("Grado", grupo1.getGrado())

    grupo2 = Grupo("Grupo 5", [], ["Alejandro", "Carlos"])

    grupo3 = Grupo()
    grupo4 = Grupo()
    grupo5 = Grupo()
    grupo3.agregarAlumno("Kelly", [])
    grupo4.agregarAlumno("Santiago", ["Jaime", "Pedro"])
    grupo5.agregarAlumno("Javier", [])


    print(grupo3.getLista())
    print(grupo4.getLista())
    print(grupo5.getLista())

    grupo3.listadoAsignaturas(as1="Ciencias", as2="Quimica", as3="Ingles")
    print(grupo3.getNumeroAsignaturas())

    grupo1.asignarNombre("Grado 1")
    print(grupo1.getGrupo())
    grupo6 = Grupo()
    grupo6.asignarNombre("Grado 6")
    print(grupo6.getGrupo())
