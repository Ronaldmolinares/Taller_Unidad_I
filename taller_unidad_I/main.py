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

    print(notas)

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

    print(notas)

    for k in notas:
        dividendo = sum(notas[k])
        divisor = len(notas[k])
        notas[k] = dividendo / divisor

    return sorted(notas, key=str.lower)


if __name__ == "__main__":
    promedio_notas = promedio_notas_asignatura(data)
    print(f"\nPROMEDIO DE NOTAS POR ASIGNATURA\n{promedio_notas}\n")
    promedio_estudiantes = promedio_notas_estudiante(data)
    print(f"\nPROMEDIO DE NOTAS POR ESTUDIANTE\n{promedio_estudiantes}\n")
