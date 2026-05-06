def pedir_nota(materia):
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {materia} (0 a 5): "))
            if 0 <= nota <= 5:
                return nota
            else:
                print(" La nota debe estar entre 0 y 5.")
        except:
            print(" Entrada inválida.")

# Ingreso de notas
md = pedir_nota("Matemáticas Discretas")
prog = pedir_nota("Programación II")
bd = pedir_nota("Bases de Datos")
pi = pedir_nota("Proyecto Integrador")

# Inasistencias
faltas = int(input("Ingrese número de inasistencias: "))

# Validar pérdida automática
if faltas >= 7:
    print("\n Estado: REPROBADO por inasistencias")
else:
    # Descuento por faltas
    descuento = 0
    if 1 <= faltas <= 3:
        descuento = 0.2
    elif 4 <= faltas <= 6:
        descuento = 0.5

    # Promedio ponderado
    promedio = (
        md * 0.30 +
        prog * 0.25 +
        bd * 0.25 +
        pi * 0.20
    )

    promedio -= descuento

    print(f"\n Promedio final: {round(promedio,2)}")

    # Estado académico
    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    # Regla especial Programación II
    if prog < 3.0:
        estado += " (Debe repetir Programación II)"

    print(" Estado:", estado)

    # Beca
    if promedio >= 4.8:
        print(" ¡Honores! Beca del 20% para el próximo semestre")
    else:
        print(" No aplica a beca")

    # Materias en riesgo (<3.0)
    print("\n Materias en riesgo:")
    if md < 3: print("- Matemáticas Discretas")
    if prog < 3: print("- Programación II")
    if bd < 3: print("- Bases de Datos")
    if pi < 3: print("- Proyecto Integrador")