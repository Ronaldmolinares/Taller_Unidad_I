# Camilo Andres Arias Tenjo
# Ronald Samir Molinares Sanabria


##########################################
### PUNTO 1, 2, 3 Y 4 DEL TALLER FINAL ###
##########################################

import json

with open("Unidad1_Reto.json", "r") as file:
    data = json.load(file)


def promedio_notas_asignatura(data):

    notas = {}

    for obj in data:
        for i in range(len(obj["asignaturas"])):
            materia = obj["asignaturas"][i]
            if materia["nombre"] not in notas:
                notas[materia["nombre"]] = []
            notas[materia["nombre"]].append(materia["nota"])

    print(f"\nPROMEDIO DE NOTAS POR ASIGNATURA\n{notas}")

    for k in notas:
        dividendo = sum(notas[k])
        divisor = len(notas[k])
        notas[k] = dividendo / divisor

    return notas


def promedio_notas_estudiante(data):
    notas = {}

    for obj in data:
        estudiante = f"{obj['apellidos']['primer_apellido']} {obj['apellidos']['segundo_apellido']} {obj['nombres']['primer_nombre']} {obj.get('nombres').get('segundo_nombre', '')}"

        notas[estudiante] = []

        for i in range(len(obj["asignaturas"])):
            materia = obj["asignaturas"][i]
            if materia["retirada"] != "Si":
                notas[estudiante].append(materia["nota"])

    print(f"\nPROMEDIO DE NOTAS POR ESTUDIANTE\n{notas}")

    for k in notas:
        dividendo = sum(notas[k])
        divisor = len(notas[k])
        notas[k] = dividendo / divisor

    return dict(sorted(notas.items()))


def mostrar_estudiantes(data):
    lista_estudiantes = []

    for obj in data:
        nombre = f"{obj['apellidos']['primer_apellido']} {obj['apellidos']['segundo_apellido']} {obj['nombres']['primer_nombre']} {obj.get('nombres').get('segundo_nombre', '')}"
        documento = str(obj["documento"])

        if obj.get("nombres").get("segundo_nombre", "") != "":
            correo_dos_nombres = f"{obj['nombres']['primer_nombre'][0]}{obj['nombres']['segundo_nombre'][0]}.{obj['apellidos']['primer_apellido']}{documento[-2:]}@uptc.edu.co"
            estudiante = {"Nombre": nombre, "Correo": correo_dos_nombres}
            lista_estudiantes.append(estudiante)

        else:
            correo_un_nombre = f"{obj['nombres']['primer_nombre'][0]}{obj['apellidos']['primer_apellido'][0]}.{obj['apellidos']['segundo_apellido']}{documento[-2:]}@uptc.edu.co"
            estudiante = {"Nombre": nombre, "Correo": correo_un_nombre}
            lista_estudiantes.append(estudiante)

    return lista_estudiantes


#############################################
### CUADERNILLO DE OPERADORES Y FUNCIONES ###
#############################################


# Codificar formula cuadratica

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

print(f"valor de a: {a}\nvalor de b: {b}\nvalor de c: {c}\n")

if a == 0:
    print("No es una ecuación cuadrática (a no puede ser 0)")
else:
    raiz = b**2 - 4 * a * c

    if raiz < 0:
        print("No hay soluciones reales (raíces complejas/imaginarias)")
    elif raiz == 0:
        x = -b / (2 * a)
        print(f"Existe una única solución real: x = {x}")
    else:
        x1 = (-b + raiz**0.5) / (2 * a)
        x2 = (-b - raiz**0.5) / (2 * a)
        print(f"El valor de x1 es: {x1}")
        print(f"El valor de x2 es: {x2}")

    def clasificar(caracter):
        """Escribir una función que reciba un carácter y evalué si el valor ingresado, corresponde a una
        vocal o a una consonante. Cuando sea vocal que retorne el valor booleano (TRUE)."""
        vocales = "aeiou"

        if caracter in vocales:
            return True

        return f"{caracter} es una consonante"


def cuadratica(a, b, c):
    """Ejercicio de ecuación cuadrática escrita en forma de función"""
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
    """
    Hacer una función que reciba una lista de números e imprima un histograma. Ejemplo:
    histogram([3,5,1]) debe mostrar:
    HHH
    HHHHH
    H
    """

    if len(lista) == 0:
        return "Sin datos para generar histograma"

    for num in lista:
        print("H" * num)


###############################
#### CUADERNILLO DE CADENAS ###
###############################

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


###############################
#### CUADERNILLO DE LISTAS ####
###############################

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


#################################
#### CUADERNILLO DE CONJUNTOS ###
#################################

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


#########################################
#### CUADERNILLO DE DICCIONARIOS ###
#########################################

words = ["apple", "bat", "bar", "atom", "book", "cat"]


def crear_diccionario(lista):
    diccionario = {}
    for palabra in lista:
        clave = palabra[0]
        if clave not in diccionario:
            diccionario[clave] = []
        diccionario[clave].append(palabra)
    return diccionario


def contador_caracteres(cadena):
    contador = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "Consonantes": 0}
    vocales = "aeiou"

    for caracter in cadena.lower():
        if caracter.isalpha():
            if caracter in vocales:
                if caracter not in contador:
                    contador[caracter] = 0
                contador[caracter] += 1
            else:
                contador["Consonantes"] += 1

    return contador


datos_empresa = "id;nombre;correo;movil;salario\n3412;Pepe Perez;pepeperez@yahoo.com;300281234;150000\n45342;Maria Melo;mariamelo@yahoo.com;315434223;300000\n5673321;Fernando Jimenez;ferjim@gmail.com;312342234;230000\n4545231;Carlos Cardenas;carloscardenas@hotmail.com;3156754323;345000"


def diccionario_empleados(datos):
    registros = datos.split("\n")
    columnas = registros[0].split(";")
    columnas.remove("id")
    diccionario = {}

    for linea in registros[1:]:
        valores = linea.split(";")
        empleado = {columnas[i]: valores[i + 1] for i in range(len(columnas))}
        diccionario[valores[0]] = empleado

    return diccionario


if __name__ == "__main__":
    print(
        "=====================PUNTO 1, 2, 3 Y 4 DEL TALLER FINAL=====================\n"
    )
    promedio_notas = promedio_notas_asignatura(data)
    print(f"******** Resultado ********\n{promedio_notas}\n")
    promedio_estudiantes = promedio_notas_estudiante(data)
    print(f"******** Resultado ********\n{promedio_estudiantes}\n")
    estudiantes = mostrar_estudiantes(data)
    print(f"\nLISTA ESTUDIANTES Y CORREO\n******** Resultado ********\n{estudiantes}")

    print("\n")
    print(
        "=====================CUADRENILLO DE OPERADORES Y FUNCIONES=====================\n"
    )
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
    datos_histograma = [3, 5, 1]
    histograma(datos_histograma)

    print("\n")
    print("=====================CUADRENILLO DE CADENAS=====================\n")
    consultas()
    ejercicio_1()
    ejercicio_2()
    ejercicio_4()
    ejercicio_6()

    print("\n")
    print("=====================CUADRENILLO DE LISTAS=====================\n")
    mostrar_empleados(Empleados)
    print("\n=== VERIFICACIÓN DE DUPLICADOS ===")
    print(f"Lista de carros: {carros}")
    print(f"¿La lista de carros tiene elementos duplicados?: {duplicados(carros)}")
    print(f"Lista de carros sin duplicados: {eliminar_duplicados(carros)}")

    print("\n")
    print("=====================CUADRENILLO DE CONJUNTOS=====================\n")

    print("\n")
    print("=====================CUADRENILLO DE DICCIONARIOS=====================\n")
    resultado = crear_diccionario(words)
    print(resultado)
    cadena = "Gestion de Datos"
    resultado_contador = contador_caracteres(cadena)
    print(f"\n{resultado_contador}")
    resultado_empleados = diccionario_empleados(datos_empresa)
    print(f"\n{resultado_empleados}")
