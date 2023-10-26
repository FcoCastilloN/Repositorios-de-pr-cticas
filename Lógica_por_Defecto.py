#La lógica por defecto es una forma de lógica no monótona que se utiliza en inteligencia artificial para representar razonamientos que permiten 
#asumir que algo es cierto a menos que se demuestre lo contrario. En otras palabras, se parte de una base de conocimiento inicial que se asume 
#como verdadera y se pueden hacer inferencias basadas en esa base de conocimiento, pero estas inferencias pueden ser revisadas o modificadas en 
#función de nueva información o excepciones.
#Un ejemplo clásico de lógica por defecto es el "problema de los pájaros" de John McCarthy. En este problema, se asume que los pájaros pueden volar
# a menos que se demuestre lo contrario.


class BaseConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas_por_defecto = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla_por_defecto(self, regla):
        self.reglas_por_defecto.append(regla)

    def verificar_hecho(self, hecho):
        if hecho in self.hechos:
            return True
        else:
            for regla in self.reglas_por_defecto:
                if regla.aplicar(self, hecho):
                    return True
            return False

class ReglaPorDefecto:
    def __init__(self, condicion, conclusion):
        self.condicion = condicion
        self.conclusion = conclusion

    def aplicar(self, base_conocimiento, hecho):
        if all(base_conocimiento.verificar_hecho(cond) for cond in self.condicion):
            base_conocimiento.agregar_hecho(self.conclusion)
            return True
        else:
            return False

# Crear una base de conocimiento con lógica por defecto
base_de_conocimiento = BaseConocimiento()

# Agregar un hecho inicial
base_de_conocimiento.agregar_hecho("pájaros_pueden_volar")

# Agregar una regla por defecto
regla = ReglaPorDefecto(["pájaros_pueden_volar"], "pájaros_vuelan")
base_de_conocimiento.agregar_regla_por_defecto(regla)

# Verificar si los pájaros vuelan
if base_de_conocimiento.verificar_hecho("pájaros_vuelan"):
    print("Los pájaros vuelan.")
else:
    print("No se sabe si los pájaros vuelan.")

# Retirar el hecho inicial (simulando nueva información)
base_de_conocimiento.hechos.remove("pájaros_pueden_volar")

# Verificar nuevamente si los pájaros vuelan
if base_de_conocimiento.verificar_hecho("pájaros_vuelan"):
    print("Los pájaros vuelan.")
else:
    print("No se sabe si los pájaros vuelan.")
