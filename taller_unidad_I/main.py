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
        divisor = len(notas[k])
        dividendo = sum(notas[k])
        notas[k] = dividendo / divisor

    return notas


if __name__ == "__main__":
    promedio_notas = promedio_notas_asignatura(data)
    print(promedio_notas)
