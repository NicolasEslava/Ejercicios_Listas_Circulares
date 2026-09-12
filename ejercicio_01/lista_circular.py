from nodo import Nodo


class ListaCircular():
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

    def mostrar(self, pasos=10):
        actual = self.inicio
        cont = 0
        while actual and cont < pasos:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            cont += 1

    def buscar(self, dato):
        if self.inicio is None:
            return False

        actual = self.inicio

        while True:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

            if actual == self.inicio:
                break

        return False

    def eliminar(self, dato):
        if self.inicio is None:
            print("lista vacia")
            return

        actual = self.inicio

        while True:

            if actual.dato == dato:

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
