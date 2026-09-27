from datetime import datetime

cadena = "20hola!-21?."
entrada = "Gestión de Datos"


def consultas():
    """
    Consulte y explique con un ejemplo las siguientes funciones para manejo de cadenas: replace,
    find, count, capitalize,title,rstrip,index, casefold.
    """
    print("=== FUNCIONES PARA MANEJO DE CADENAS ===")
    print("\n1. Función replace()")
    # Remplaza un patrón de texto por otro. Ejemplo: "20hola!-21?." reemplaza "20" por "Bienvenido"
    print(f"Original: {cadena}")
    print(f"Resultado: {cadena.replace('20', 'Bienvenido')}")

    print("\n2. Función find()")
    # Busca un patrón de texto y devuelve la posición de la primera coincidencia. Ejemplo: "20hola!-21?." busca "hola"
    print(f"Posición de la primera coincidencia de 'hola': {cadena.find('hola')}")

    print("\n3. Función count()")
    # Cuenta el número de veces que aparece un patrón de texto. Ejemplo: "20hola!-21?." cuenta cuántas veces aparece "2"
    print(f"Cantidad de apariciones de '2': {cadena.count('2')}")

    print("\n4. Función capitalize()")
    # Convierte la primera letra de la cadena en mayúscula y el resto en minúscula. Ejemplo: "Gestión de Datos" se convierte en "Gestión de datos"
    print(f"Resultado con la primera letra en mayúscula: {entrada.capitalize()}")

    print("\n5. Función title()")
    # Convierte la primera letra de cada palabra en mayúscula. Ejemplo: "Gestión de Datos" se convierte en "Gestión De Datos"
    print(
        f"Resultado con la primera letra de cada palabra en mayúscula: {entrada.title()}"
    )

    print("\n6. Función rstrip()")
    # Elimina los espacios en blanco al final de la cadena. Ejemplo: "  hola  " se convierte en "  hola"
    print(f"Original: {'  hola  '}|")
    print(f"Resultado sin espacios al final: {'  hola  '.rstrip()}|")

    print("\n7. Función index()")
    # Busca un patrón de texto y devuelve la posición de la primera coincidencia. Ejemplo: "20hola!-21?." busca "hola"
    print(f"Índice de la primera coincidencia de 'hola': {cadena.index('hola')}")

    print("\n8. Función casefold()")
    # Convierte la cadena a minúsculas (con mas soporte para caracteres especiales que .lower()). Ejemplo: "Gestión de Datos" se convierte en "gestión de datos"
    print(f"Resultado en minúsculas: {entrada.casefold()}")


def ejercicio_1():
    print("\n=== EJERCICIO 1: VARIABLE DE CADENA ===")
    print(f"Valor de la variable cadena: {cadena}")


def ejercicio_2():
    print("\n=== EJERCICIO 2: ACCESO POR ÍNDICE ===")
    print(f"Carácter en el índice 4: {cadena[4]}")
    print(f"Carácter en el índice 7: {cadena[7]}")


def ejercicio_4():
    """
    Utilizar algún método para dividir una frase en palabras, en letras reemplazar, fusionar o unir con
        otros patrones.
        Entrada: "Gestión de Datos"
        Salidas:
        ['Gestión', 'de', 'Datos']
        Analítica de Datos
        G-e-s-t-i-ó-n- -d-e- -D-a-t-o-s
        Gestión-de-Datos
    """
    print("\n=== EJERCICIO 4: DIVIDIR, REEMPLAZAR Y UNIR ===")

    print(f"Frase de entrada: {entrada}\n")

    funcion_split = entrada.split()
    print(f"1. Frase dividida en palabras (split): {funcion_split}")

    funcion_replace = entrada.replace("Gestión", "Analítica")
    print(f"2. Palabra reemplazada (replace): {funcion_replace}")

    texto_separado = "-".join(entrada)
    caracter_guion = "-".join(funcion_split)
    print(f"3. Letras unidas con guion (join): {texto_separado}")
    print(f"4. Palabras unidas con guion (join): {caracter_guion}")


def ejercicio_6():
    """Obtener la fecha actual y luego pasarla a tipo cadena para extraerle el mes: Por ejemplo a partir
    de la fecha: 2024-03-07 imprimir: Mes 03.
    """
    print("\n=== EJERCICIO 6: FECHA Y EXTRACCIÓN DEL MES ===")
    now = datetime.now()
    fecha_str = now.strftime("%Y-%m-%d")
    mes = fecha_str[5:7]
    print(f"Fecha actual convertida a cadena: {fecha_str}")
    print(f"Mes extraído: {mes}")


if __name__ == "__main__":
    consultas()
    ejercicio_1()
    ejercicio_2()
    ejercicio_4()
    ejercicio_6()
