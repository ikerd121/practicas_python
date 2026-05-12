lista_alumno=[]

for numero in range(1,6):
    print(f"introduce el alumno {numero}")
    nombre=input("introduce el nombre del alumno: ")
    apellido=input("introduce el apellido del alumno: ")
    persona={
        "nombre": nombre,
        "apellido": apellido
    }
    lista_alumno.append(persona)

for alumno in lista_alumno:
    print(alumno["nombre"])
    print(alumno["apellido"])

