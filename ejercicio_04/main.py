from lista_circular import ListaCircular
from empleado import Empleado


empleado1 = Empleado("Nicolas", "CEO")
empleado2 = Empleado("Felipe", "Arquitecto")
empleado3 = Empleado("Estefany", "Ingeniera")
empleado4 = Empleado("Carlos", "Contador")


lista = ListaCircular()


lista.agregar(empleado1)
lista.agregar(empleado2)
lista.agregar(empleado3)
lista.agregar(empleado4)

print("ORIGINAL LIST")
lista.mostrar()

print("ELIMINAR")
lista.eliminar("Felipe")


lista.mostrar()
