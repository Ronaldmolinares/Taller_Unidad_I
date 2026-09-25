def clasificar(caracter):
    vocales = "aeiou"

    if caracter in vocales:
        return True

    return f"{caracter} es una consonante"


def cuadratica(a, b, c):
    if a == 0:
        return "No es una ecuación cuadrática (a no puede ser 0)"
    else:
        raiz = b**2 - 4 * a * c

        if raiz < 0:
            return "No hay soluciones reales (raíces complejas/imaginarias)"
        elif raiz == 0:
            x = -b / (2 * a)
            return f"Existe una única solución real: x = {x}"
        else:
            x1 = (-b + raiz**0.5) / (2 * a)
            x2 = (-b - raiz**0.5) / (2 * a)
            return f"El valor de x1 es: {x1} y el valor de x2 es: {x2}"


def histograma(lista):

    if len(lista) == 0:
        return "Sin datos para generar histograma"

    for num in lista:
        print("H" * num)


if __name__ == "__main__":
    vocal = "a"
    consonante = "N"
    print(
        f"Función Vocal - Consonante:\nLetra {vocal} = {clasificar(vocal)}\nLetra {consonante} = {clasificar(consonante)}"
    )

    a = -1
    b = 2
    c = 3
    print(
        f"\nFunción Cuadratica:\nvalor de a: {a}\nvalor de b: {b}\nvalor de c: {c}\n{cuadratica(a, b, c)}\n"
    )

    print("Función Histograma:")
    datos_histograma = [9, 3, 4]
    histograma(datos_histograma)
