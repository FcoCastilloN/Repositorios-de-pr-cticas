

class AgenteLogico:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomar_decision(self, informacion):
        if "informacion_importante" in informacion:
            decision = "Tomar acción A"
        else:
            decision = "Tomar acción B"
        return decision

# Crear un agente lógico
agente = AgenteLogico("Agente1")

# Simular una situación con información
informacion = {"informacion_importante": True}

# El agente toma una decisión en función de la información
decision = agente.tomar_decision(informacion)

print(f"{agente.nombre} decide: {decision}")
