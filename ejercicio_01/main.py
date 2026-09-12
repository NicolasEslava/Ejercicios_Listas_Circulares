from lista_circular import ListaCircular

lista = ListaCircular()

for datos in (10, 20, 30, 40):
    lista.agregar(datos)

lista.mostrar()
resultado = lista.buscar(30)
print("la variable esta en la lista: ", resultado)

lista.eliminar(30)
lista.mostrar()
