"""
Diferencia entre set y frozenset en Python:
Un set es una colección mutable de elementos únicos, mientras que un frozenset es una colección
inmutable de elementos únicos. Esto significa que los elementos de un set pueden ser modificados (agregados o eliminados),
mientras que los elementos de un frozenset no pueden ser cambiados después de su creación.
"""


def metodo_intersection_update():
    """Modifica el conjunto original dejando solo los elementos que tiene en común con otro conjunto (intersección)"""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    tus_carros = {"Ferrari", "Mazda", "Bugatti"}
    mis_carros.intersection_update(tus_carros)
    print(mis_carros)  # {'Ferrari', 'Bugatti'}


def metodo_isdisjoint():
    """Devuelve True si los dos conjuntos no tienen ningún elemento en común. Si tienen aunque sea uno, devuelve False."""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    tus_carros = {"Mazda", "Toyota", "Honda"}
    resultado = mis_carros.isdisjoint(tus_carros)
    print(resultado)  # True


def metodo_issubset():
    """Devuelve True si todos los elementos del conjunto original están en el otro conjunto (subconjunto)"""
    mis_carros = {"BMW", "Ferrari"}
    tus_carros = {"BMW", "Ferrari", "Bugatti"}
    resultado = mis_carros.issubset(tus_carros)
    print(resultado)  # True


def metodo_issuperset():
    """Devuelve True si todos los elementos del otro conjunto están en el conjunto original (superconjunto)"""
    carrito_compras = {"queso", "tomate", "harina", "jamón"}
    ingredientes_pizza = {"queso", "tomate"}
    print(carrito_compras.issuperset(ingredientes_pizza))  # True


def metodo_pop():
    """Elimina y devuelve un elemento aleatorio del conjunto. Si el conjunto está vacío, lanza un KeyError."""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    elemento_eliminado = mis_carros.pop()
    print(f"Elemento eliminado: {elemento_eliminado}")
    print(mis_carros)


def metodo_remove():
    """Elimina un elemento específico del conjunto. Si el elemento no existe, lanza un KeyError."""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    mis_carros.remove("Ferrari")
    print(mis_carros)  # {'BMW', 'Bugatti'}


def metodo_symmetric_difference():
    """Devuelve un nuevo conjunto con los elementos que están en uno de los conjuntos pero no en ambos (diferencia simétrica)"""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    tus_carros = {"Ferrari", "Mazda", "Bugatti"}
    resultado = mis_carros.symmetric_difference(tus_carros)
    print(resultado)  # {'BMW', 'Mazda'}


def metodo_symmetric_difference_update():
    """Modifica el conjunto original dejando solo los elementos que están en uno de los conjuntos pero no en ambos (diferencia simétrica)"""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    tus_carros = {"Ferrari", "Mazda", "Bugatti"}
    mis_carros.symmetric_difference_update(tus_carros)
    print(mis_carros)  # {'BMW', 'Mazda'}


def metodo_union():
    """Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos (unión)"""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    tus_carros = {"Ferrari", "Mazda", "Bugatti"}
    resultado = mis_carros.union(tus_carros)
    print(resultado)  # {'BMW', 'Ferrari', 'Mazda', 'Bugatti'}


def metodo_update():
    """Modifica el conjunto original agregando todos los elementos de otro conjunto (unión)"""
    mis_carros = {"BMW", "Ferrari", "Bugatti"}
    tus_carros = {"Lamborgini", "Mazda", "Bugatti"}
    mis_carros.update(tus_carros)
    print(mis_carros)  # {'BMW', 'Ferrari', 'Lamborgini', 'Mazda', 'Bugatti'}
