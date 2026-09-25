from datetime import datetime

cadena = "20hola!-21?."
entrada = "Gestión de Datos"


def ejercicio_1():
    print("Ejercicio 1")
    print(f"Variale: {cadena}")


def ejercicio_2():
    print("\nEjercicio 2")
    print(f"Indice 4: {cadena[4]}\nIndice 7: {cadena[7]}")


def ejercicio_4():
    print("\nEjercicio 4")

    print(f"Cadena original: {entrada}\n")

    funcion_split = entrada.split()
    print(f"Función Split: {funcion_split}\n")

    funcion_replace = entrada.replace("Gestión", "Analitica")
    print(f"Función Replace: {funcion_replace}\n")

    print("Función Join:")
    texto_separado = "-".join(entrada)
    print(texto_separado)
    print(texto_separado.replace(" ", ""))
    caracter_guion = "-".join(funcion_split)
    print(caracter_guion)


def ejercicio_6():
    print("\nEjercicio 6:")
    now = datetime.now()
    print(now)
    fecha_str = now.strftime("%Y-%m-%d")
    mes = fecha_str[5:7]
    print(f"Mes {mes}")


if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
    ejercicio_4()
    ejercicio_6()
