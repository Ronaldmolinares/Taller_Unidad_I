nombres = ["Luis", "Pedro", "Lucia"]
Edades = [20, 18, 30]
Peso = [55.6, 60, 65.8]
Empleados = [nombres, Edades, Peso]
carros = [
    "Mazda",
    "Toyota",
    "Chevrolet",
    "Mazda",
    "Toyota",
    "Chevrolet",
    "Mazda",
    "Toyota",
    "Chevrolet",
    "Mazda",
    "Toyota",
    "Chevrolet",
]


def funcion_copy():
    """Copy crea una lista nueva (referencia en memoria) con los mismo elementos de la original"""
    print("Uso copy:")
    original = [1, 2, 3]
    copia = original.copy()
    copia.append(4)
    print(original)  # [1, 2, 3]  (No cambia)
    print(copia)  # [1, 2, 3, 4]


def funcion_remove():
    """remove elimina el primer elemento que coincida con el valor especificado"""
    numeros = [10, 20, 30, 20]
    numeros.remove(20)
    print(numeros)  # [10, 30, 20] (Solo borró el primero)


def funcion_clear():
    """clear elimina todos los elementos de la lista"""
    numeros = [10, 20, 30, 40]
    numeros.clear()
    print(numeros)  # [] (Vacía la lista)


def funcion_del():
    """del elimina un elemento por su índice"""
    numeros = [10, 20, 30, 40]
    del numeros[1]
    print(numeros)  # [10, 30, 40] (Elimina el elemento en el índice 1)


def funcion_in():
    """in verifica si un elemento está en la lista"""
    numeros = [10, 20, 30, 40]
    print(20 in numeros)  # True
    print(50 in numeros)  # False


def funcion_append_vs_extend():
    print("Uso append vs extend:")
    """Agrega un solo objeto al final de la lista, tal y como se lo pases. Si le pasas otra lista, mete la lista entera dentro."""
    # Uso de append
    lista_a = [1, 2, 3]
    lista_a.append([4, 5])
    print(lista_a)  # Resultado: [1, 2, 3, [4, 5]]

    """Desempaqueta o "desarma" un iterable (lista, tupla, etc.) y agrega cada uno de sus elementos uno por uno al final."""
    # Uso de extend
    lista_b = [1, 2, 3]
    lista_b.extend([4, 5])
    print(lista_b)  # Resultado: [1, 2, 3, 4, 5]


def mostrar_empleados(empleados):
    print("Empleados")
    for i in range(len(empleados[0])):
        print(
            f"Empleado_{i + 1}: {empleados[0][i]}, Edad: {empleados[1][i]}, Peso: {empleados[2][i]}"
        )


def duplicados(lista):

    for i in lista:
        if lista.count(i) > 1:
            return True

    return False


def eliminar_duplicados(lista):
    return list(set(lista))


def eliminar_duplicados_2(lista):
    sin_duplicados = []
    for i in lista:
        if i not in sin_duplicados:
            sin_duplicados.append(i)
    return sin_duplicados


if __name__ == "__main__":
    mostrar_empleados(Empleados)
    print(duplicados(carros))
    print(eliminar_duplicados(carros))
    print(eliminar_duplicados_2(carros))
