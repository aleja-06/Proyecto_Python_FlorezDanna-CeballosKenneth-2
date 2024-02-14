import json

def cargar_campers_desde_archivo():
    try:
        with open("campers.json", "r") as file:
            campers = json.load(file)
    except FileNotFoundError:
        campers = []
    return campers

def guardar_campers_en_archivo(campers):
    with open("campers.json", "w") as file:
        json.dump(campers, file, indent=2)

def crear_nuevo_camper():
    nombre = input("Ingrese el nombre del Camper: ")
    tipo = input("Ingrese el tipo de Camper: ")
    color = input("Ingrese el color del Camper: ")

    nuevo_camper = {
        "nombre": nombre,
        "tipo": tipo,
        "color": color
    }

    campers = cargar_campers_desde_archivo()
    campers.append(nuevo_camper)
    guardar_campers_en_archivo(campers)

    print(f"¡Camper '{nombre}' creado y guardado exitosamente!")

def listar_campers():
    campers = cargar_campers_desde_archivo()

    if not campers:
        print("No hay campers registrados.")
    else:
        print("Lista de Campers:")
        for camper in campers:
            print(f"Nombre: {camper['nombre']}, Tipo: {camper['tipo']}, Color: {camper['color']}")

def modificar_camper():
    nombre_a_modificar = input("Ingrese el nombre del Camper a modificar: ")
    campers = cargar_campers_desde_archivo()

    encontrado = False
    for camper in campers:
        if camper['nombre'] == nombre_a_modificar:
            nuevo_nombre = input("Ingrese el nuevo nombre del Camper: ")
            nuevo_tipo = input("Ingrese el nuevo tipo del Camper: ")
            nuevo_color = input("Ingrese el nuevo color del Camper: ")

            camper['nombre'] = nuevo_nombre
            camper['tipo'] = nuevo_tipo
            camper['color'] = nuevo_color

            encontrado = True
            break

    if encontrado:
        guardar_campers_en_archivo(campers)
        print(f"Camper '{nombre_a_modificar}' modificado exitosamente.")
    else:
        print(f"No se encontró el Camper '{nombre_a_modificar}'.")

# Menú principal
while True:
    print("\nMENU:")
    print("1. Crear Camper")
    print("2. Listar Campers")
    print("3. Modificar Camper")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        crear_nuevo_camper()
    elif opcion == "2":
        listar_campers()
    elif opcion == "3":
        modificar_camper()
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
