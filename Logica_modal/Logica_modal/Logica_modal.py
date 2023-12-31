# La l�gica modal se basa en el uso de operadores modales, como "necesario" y "posible", que permiten expresar declaraciones condicionales y 
# cuantificar sobre diferentes mundos posibles. Es especialmente �til en la representaci�n del conocimiento, el razonamiento y la planificaci�n 
# en la inteligencia artificial.

#En la l�gica modal, algunos de los operadores modales m�s comunes son:

#(necesario): Representa que una proposici�n es necesariamente verdadera en todos los mundos posibles.
#(posible): Representa que una proposici�n es verdadera en al menos un mundo posible.



from pymodal.modal_logic import World, KB

# Crear dos mundos posibles
world1 = World("Mundo 1")
world2 = World("Mundo 2")

# Definir una base de conocimientos (KB)
kb = KB()

# Afirmar una proposici�n en el primer mundo
kb.tell(world1, "P")

# Afirmar una proposici�n en el segundo mundo
kb.tell(world2, "Q")

# Comprobar si "P" es necesario
print(f"�P es necesario? {kb.necessarily_true('P')}")

# Comprobar si "Q" es posible
print(f"�Q es posible? {kb.possibly_true('Q')}")

