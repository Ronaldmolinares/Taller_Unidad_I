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
