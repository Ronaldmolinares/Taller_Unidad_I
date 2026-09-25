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
    resultado = crear_diccionario(words)
    print(resultado)

    cadena = "Gestion de Datos"
    resultado_contador = contador_caracteres(cadena)
    print(f"\n{resultado_contador}")

    resultado_empleados = diccionario_empleados(datos_empresa)
    print(f"\n{resultado_empleados}")
