from nodo import Nodo


class ListaCircular:
    def __init__(self):
        self.inicio = None

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.inicio is None:
            self.inicio = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
        else:
            ultimo = self.inicio.anterior

            nuevo.siguiente = self.inicio
            nuevo.anterior = ultimo

            ultimo.siguiente = nuevo
            self.inicio.anterior = nuevo

    def mostrar(self):
        if self.inicio == None:
            print("lista vacia")
            return

        actual = self.inicio

        while True:
            actual.dato.mostrar_info()
            actual = actual.siguiente

            if actual == self.inicio:
                break

    def eliminar(self, dato):
        if self.inicio is None:
            print("lista vacia")
            return

        actual = self.inicio

        while True:

            if actual.dato.nombre == dato:

                # Si solamente existe un nodo
                if actual.siguiente == actual:
                    self.inicio = None
                    return

                # Si eliminamos el inicio
                if actual == self.inicio:
                    self.inicio = actual.siguiente

                anterior = actual.anterior
                siguiente = actual.siguiente

                anterior.siguiente = siguiente
                siguiente.anterior = anterior

                return

            actual = actual.siguiente

            if actual == self.inicio:
                break

        print("Dato no encontrado")

    def buscar(self, dato):
        if self.inicio is None:
            print("Lista vacia")
            return None

        actual = self.inicio

        while True:
            if actual.dato.nombre == dato:
                print("El dato si esta en la lista")
                return actual.dato

            actual = actual.siguiente

            if actual == self.inicio:
                break

        print("el dato no se encuentra en la lista")
        return None
