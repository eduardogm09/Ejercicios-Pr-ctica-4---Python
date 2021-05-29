alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos a guardar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Ingrese una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Ingrese una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))

def aprobacion(nota):
    if nota > 7:
        return "Promociona"
    else:
        if nota < 4:
            return "Aplazado"
        else:
            if 4 <= nota and nota  <= 7:
                return "Aprobado"

