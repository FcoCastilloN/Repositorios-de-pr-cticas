#La lógica de orden superior en inteligencia artificial se refiere a la capacidad de tratar funciones como ciudadanos de primera clase. Esto significa que 
#puedes pasar funciones como argumentos a otras funciones, devolver funciones desde funciones, y almacenar funciones en variables. Esto es una característica 
#fundamental en muchos lenguajes de programación, incluido Python, y es especialmente útil en la programación funcional y en la construcción de algoritmos más 
#flexibles y genéricos.
#Un ejemplo sencillo de lógica de orden superior en Python es el uso de funciones lambda (funciones anónimas) y funciones de orden superior como map() y filter(). 
#Estas funciones pueden tomar otras funciones como argumentos.


#Ejemplo 1: Usando map() con una función de orden superior en Python:
# Función de orden superior
#En este ejemplo, la función cuadrado es una función de orden superior porque puede aplicarse a una lista de números utilizando map().


def cuadrado(x):
    return x ** 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar la función de orden superior a cada elemento de la lista usando map()
resultados = list(map(cuadrado, numeros))

print(resultados)

