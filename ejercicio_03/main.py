from lista_circular import ListaCircular
from empleado import Empleado

empleado1 = Empleado("Nicolas", "CEO")
empleado2 = Empleado("Felipe", "Arquitecto")
empleado3 = Empleado("Estefany", "Ingeniera")

lista = ListaCircular()

for empleados in (empleado1, empleado2, empleado3):
    lista.agregar(empleados)

lista.mostrar()
