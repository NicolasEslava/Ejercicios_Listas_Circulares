from nodo import Nodo


class ListaCircular:
    def __init__(self):
        self.inicio = None

    def agregar(self, persona):
        nuevo = Nodo(persona)
        if self.inicio == None:
            self.inicio = nuevo
            nuevo.siguiente = self.inicio
        else:
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.inicio

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
