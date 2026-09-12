from lista_circular import ListaCircular
from estudiante import Estudiante


# Crear Estudiantes
Estudiante1 = Estudiante("Nicolas", "Ingenieria")
Estudiante2 = Estudiante("Felipe", "Arquitectura")
Estudiante3 = Estudiante("Estefany", "Ingenieria")
Estudiante4 = Estudiante("Carlos", "Contaduria")


# Crear lista circular
lista = ListaCircular()


# Agregar Estudiantes
lista.agregar(Estudiante1)
lista.agregar(Estudiante2)
lista.agregar(Estudiante3)
lista.agregar(Estudiante4)


print("LISTA DE EstudianteS")
lista.mostrar()


print("\nBUSCAR Estudiante")

Estudiante_encontrado = lista.buscar("Estefany")

if Estudiante_encontrado:
    print("Estudiante encontrado:")
    Estudiante_encontrado.mostrar_info()


print("\nELIMINAR Estudiante Felipe")

lista.eliminar("Felipe")

print("\nLISTA DESPUES DE ELIMINAR")
lista.mostrar()
