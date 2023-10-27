#La lógica no monótona es un enfoque en la lógica y la inteligencia artificial que se utiliza para representar el razonamiento que no sigue 
#la lógica clásica monotónica. En la lógica monótona, se asume que si una afirmación es cierta, seguirá siendo cierta al agregar más información. 
#En cambio, en la lógica no monótona, las afirmaciones pueden dejar de ser ciertas cuando se agrega nueva información.

#Un ejemplo común de lógica no monótona es el "mundo del cierre" (closed world assumption), donde se asume que algo es falso a menos que se pueda
#demostrar que es cierto. Esto es útil en situaciones en las que no se tiene información completa y es necesario hacer suposiciones lógicas basadas
#en la información disponible.

class BaseConocimiento:
    def __init__(self):
        self.hechos = set()

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def eliminar_hecho(self, hecho):
        self.hechos.discard(hecho)

    def verificar_hecho(self, hecho):
        return hecho in self.hechos

# Crear una base de conocimiento
base_de_conocimiento = BaseConocimiento()

# Agregar hechos iniciales
base_de_conocimiento.agregar_hecho("pájarosvuelan")
base_de_conocimiento.agregar_hecho("pingüinosnovuelan")

# Verificar si los pájaros vuelan (lógica monótona)
if base_de_conocimiento.verificar_hecho("pájaros_vuelan"):
    print("Los pájaros vuelan.")
else:
    print("Los pájaros no vuelan.")

# Agregar información adicional
base_de_conocimiento.agregar_hecho("pingüinos_pueden_nadar")

# Verificar si los pájaros vuelan con la nueva información (lógica no monótona)
if base_de_conocimiento.verificar_hecho("pájaros_vuelan"):
    print("Los pájaros vuelan.")
else:
    print("Los pájaros no vuelan.")

# Verificar si los pingüinos vuelan con la nueva información (lógica no monótona)
if base_de_conocimiento.verificar_hecho("pingüinos_no_vuelan"):
    print("Los pingüinos no vuelan.")
else:
    print("Los pingüinos pueden volar.")
