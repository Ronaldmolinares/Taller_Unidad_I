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


if __name__ == "__main__":
    promedio_notas = promedio_notas_asignatura(data)
    print(f"******** Resultado ********\n{promedio_notas}\n")
    promedio_estudiantes = promedio_notas_estudiante(data)
    print(f"******** Resultado ********\n{promedio_estudiantes}\n")
    estudiantes = mostrar_estudiantes(data)
    print(f"\nLISTA ESTUDIANTES Y CORREO\n******** Resultado ********\n{estudiantes}")
