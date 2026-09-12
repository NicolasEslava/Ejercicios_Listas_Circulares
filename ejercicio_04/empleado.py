from persona import Persona


class Empleado (Persona):
    def __init__(self, nombre, cargo):
        super().__init__(nombre)
        self.cargo = cargo

    def mostrar_info(self):
        print(
            f"mi nombre es {self.nombre} y mi cargo en la empresa es {self.cargo}")
