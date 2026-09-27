# Diccionario para relacionar nombres de estudiantes con sus notas
estudiantes = {
    "Pedro": 8,
    "Maria": 9,
    "Jose": 7,
    "Bryan": 10
}

# Agregar un nuevo estudiante al diccionario
estudiantes["Ana"] = 9

# Mostrar la información almacenada
print("--- Lista de estudiantes registrados ---")
for nombre, nota in estudiantes.items():
    print(f"{nombre}: {nota}")

# Buscar un estudiante por nombre
buscar = input("\nIngrese el nombre de un estudiante para consultar su nota: ")

if buscar in estudiantes:
    print(f"{buscar} tiene una nota de {estudiantes[buscar]}")
else:
    print(f"{buscar} no está registrado.")