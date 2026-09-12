from persona import Persona


class Estudiante (Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def mostrar_info(self):
        print(
            f"mi nombre es {self.nombre} y la carrera que estoy estudiando es {self.carrera}")
