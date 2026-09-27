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
]

"""Consulte el uso de las siguientes funciones y operadores de listas: copy, remove, del, clear, IN,
diferencia entre append y extend"""


def funcion_copy():
    """Copy crea una lista nueva (referencia en memoria) con los mismo elementos de la original"""
    print("\n=== copy(): copiar una lista ===")
    original = [1, 2, 3]
    copia = original.copy()
    copia.append(4)
    print(f"Lista original (no cambia): {original}")
    print(f"Copia después de agregar 4: {copia}")


def funcion_remove():
    """remove elimina el primer elemento que coincida con el valor especificado"""
    print("\n=== remove(): eliminar la primera coincidencia ===")
    numeros = [10, 20, 30, 20]
    numeros.remove(20)
    print(f"Lista después de eliminar el primer 20: {numeros}")


def funcion_clear():
    """clear elimina todos los elementos de la lista"""
    print("\n=== clear(): vaciar una lista ===")
    numeros = [10, 20, 30, 40]
    numeros.clear()
    print(f"Lista después de eliminar todos sus elementos: {numeros}")


def funcion_del():
    """del elimina un elemento por su índice"""
    print("\n=== del(): eliminar por índice ===")
    numeros = [10, 20, 30, 40]
    del numeros[1]
    print(f"Lista después de eliminar el elemento del índice 1: {numeros}")


def funcion_in():
    """in verifica si un elemento está en la lista"""
    print("\n=== in: comprobar si un elemento pertenece a la lista ===")
    numeros = [10, 20, 30, 40]
    print(f"¿El número 20 está en la lista?: {20 in numeros}")
    print(f"¿El número 50 está en la lista?: {50 in numeros}")


def funcion_append_vs_extend():
    print("\n=== Diferencia entre append() y extend() ===")
    """Agrega un solo objeto al final de la lista, tal y como se lo pases. Si le pasas otra lista, mete la lista entera dentro."""
    # Uso de append
    lista_a = [1, 2, 3]
    lista_a.append([4, 5])
    print(f"append() agrega la lista como un solo elemento: {lista_a}")

    """Desempaqueta o "desarma" un iterable (lista, tupla, etc.) y agrega cada uno de sus elementos uno por uno al final."""
    # Uso de extend
    lista_b = [1, 2, 3]
    lista_b.extend([4, 5])
    print(f"extend() agrega cada elemento de la lista: {lista_b}")


def mostrar_empleados(empleados):
    """Realizar una función que reciba como parámetro la lista de los empleados. Mostrar la
    información de los empleados con el formato específico:
    nombres=['Luis','Pedro','Lucia']
    edades=[20,18,30]
    peso=[55.6,60,65.8]
    empleados=[nombres,edades,peso]
    Formato de salida:
    Empleado # 1: Nombre: Luis, Edad: 20, Peso: 55.6
    Empleado # 2: Nombre: Pedro, Edad: 18, Peso: 60
    Empleado # 3: Nombre; Lucia, Edad: 30, Peso: 65.8"""
    print("\n=== INFORMACIÓN DE LOS EMPLEADOS ===")
    for i in range(len(empleados[0])):
        print(
            f"Empleado # {i + 1}: Nombre: {empleados[0][i]}, Edad: {empleados[1][i]}, Peso: {empleados[2][i]}"
        )


def duplicados(lista):
    """Crear una función que revise una lista, devolviendo true o flase en el caso que haya algún
    elemento duplicado. No se debe modificar la lista."""
    for i in lista:
        if lista.count(i) > 1:
            return True

    return False


def eliminar_duplicados(lista):
    """Hacer una función que elimine duplicados de una lista."""
    return list(set(lista))


if __name__ == "__main__":
    mostrar_empleados(Empleados)
    print("\n=== VERIFICACIÓN DE DUPLICADOS ===")
    print(f"Lista de carros: {carros}")
    print(f"¿La lista de carros tiene elementos duplicados?: {duplicados(carros)}")
    print(f"Lista de carros sin duplicados: {eliminar_duplicados(carros)}")
