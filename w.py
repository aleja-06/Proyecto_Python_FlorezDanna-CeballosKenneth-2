import json
import os

def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def cargar_datos():
    try:
        with open('campers_trainers.json', 'r') as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = {"campers": [], "trainers": []}
    return datos

def guardar_datos(datos):
    with open('campers_trainers.json', 'w') as file:
        json.dump(datos, file)

def obtener_opcion_valida(mensaje, rango_opciones):
    while True:
        opcion = input(mensaje)
        if opcion.isdigit() and int(opcion) in rango_opciones:
            return int(opcion)
        print("Por favor, ingresa un dígito válido dentro del intervalo.")

def crear_camper(datos):
    limpiar_pantalla()
    print("==== Crear Camper ====")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    id_camper = input("ID: ")
    direccion = input("Dirección: ")
    acudiente = input("Acudiente: ")
    telefono_celular = input("Teléfono Celular: ")
    telefono_fijo = input("Teléfono Fijo: ")

    nuevo_camper = {
        "nombre": nombre,
        "apellido": apellido,
        "id": id_camper,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono_celular": telefono_celular,
        "telefono_fijo": telefono_fijo
    }

    datos["campers"].append(nuevo_camper)
    guardar_datos(datos)
    print("Camper creado exitosamente.")
    input("Presiona Enter para volver al menú.")

def modificar_trainer(datos):
    limpiar_pantalla()
    print("==== Modificar Trainer ====")
    id_trainer = input("Ingresa la ID del Trainer que deseas modificar: ")
    encontrado = False
    for trainer in datos["trainers"]:
        if trainer["id"] == id_trainer:
            print(f"Datos actuales de {trainer['nombre']} {trainer['apellido']}:")
            print(f"Nombre: {trainer['nombre']}")
            print(f"Apellido: {trainer['apellido']}")
            print(f"Horario: {trainer['horario']}")
            print("\nIngrese los nuevos datos:")
            trainer["nombre"] = input("Nombre: ")
            trainer["apellido"] = input("Apellido: ")
            trainer["horario"] = input("Horario: ")
            encontrado = True
            guardar_datos(datos)
            print("Trainer modificado exitosamente.")
            break
    if not encontrado:
        print("No se encontró un Trainer con esa ID.")
    input("Presiona Enter para volver al menú.")

def eliminar_camper(datos):
    limpiar_pantalla()
    print("==== Eliminar Camper ====")
    id_camper = input("Ingresa la ID del Camper que deseas eliminar: ")
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            datos["campers"].remove(camper)
            guardar_datos(datos)
            print("Camper eliminado exitosamente.")
            input("Presiona Enter para volver al menú.")
            return
    print("No se encontró un Camper con esa ID.")
    input("Presiona Enter para volver al menú.")

def eliminar_trainer(datos):
    limpiar_pantalla()
    print("==== Eliminar Trainer ====")
    id_trainer = input("Ingresa la ID del Trainer que deseas eliminar: ")
    for trainer in datos["trainers"]:
        if trainer["id"] == id_trainer:
            datos["trainers"].remove(trainer)
            guardar_datos(datos)
            print("Trainer eliminado exitosamente.")
            input("Presiona Enter para volver al menú.")
            return
    print("No se encontró un Trainer con esa ID.")
    input("Presiona Enter para volver al menú.")

def listar_campers(datos):
    limpiar_pantalla()
    print("==== Listar Campers ====")
    if datos["campers"]:
        for camper in datos["campers"]:
            print(f"ID: {camper['id']} - {camper['nombre']} {camper['apellido']}")
    else:
        print("No hay campers registrados.")
    input("Presiona Enter para volver al menú.")

def modificar_camper(datos):
    limpiar_pantalla()
    print("==== Modificar Camper ====")
    id_camper = input("Ingresa la ID del Camper que deseas modificar: ")
    encontrado = False
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            print(f"Datos actuales de {camper['nombre']} {camper['apellido']}:")
            print(f"Nombre: {camper['nombre']}")
            print(f"Apellido: {camper['apellido']}")
            print(f"Dirección: {camper['direccion']}")
            print(f"Acudiente: {camper['acudiente']}")
            print(f"Teléfono Celular: {camper['telefono_celular']}")
            print(f"Teléfono Fijo: {camper['telefono_fijo']}")
            print("\nIngrese los nuevos datos:")
            camper["nombre"] = input("Nombre: ")
            camper["apellido"] = input("Apellido: ")
            camper["direccion"] = input("Dirección: ")
            camper["acudiente"] = input("Acudiente: ")
            camper["telefono_celular"] = input("Teléfono Celular: ")
            camper["telefono_fijo"] = input("Teléfono Fijo: ")
            encontrado = True
            guardar_datos(datos)
            print("Camper modificado exitosamente.")
            break
    if not encontrado:
        print("No se encontró un Camper con esa ID.")
    input("Presiona Enter para volver al menú.")

def crear_trainer(datos):
    limpiar_pantalla()
    print("==== Crear Trainer ====")
    nombre = input("Nombre del Trainer: ")
    apellido = input("Apellido del Trainer: ")
    horario = input("Horario del Trainer (mañana/tarde): ")
    id_trainer = input("ID del Trainer: ")

    nuevo_trainer = {
        "nombre": nombre,
        "apellido": apellido,
        "horario": horario,
        "id": id_trainer
    }

    datos["trainers"].append(nuevo_trainer)
    guardar_datos(datos)
    print("Trainer creado exitosamente.")
    input("Presiona Enter para volver al menú.")

def ver_horario(datos):
    limpiar_pantalla()
    print("==== Ver Horario del Trainer ====")
    id_trainer = input("Ingresa la ID del Trainer: ")
    encontrado = False
    for trainer in datos["trainers"]:
        if trainer["id"] == id_trainer:
            print(f"Horario de {trainer['nombre']} {trainer['apellido']}: {trainer['horario']}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un Trainer con esa ID.")
    input("Presiona Enter para volver al menú.")

def menu_coordinador(datos):
    while True:
        limpiar_pantalla()
        print("===== Menú Coordinador =====")
        print("1. Configuración Campers")
        print("2. Configuración Trainers")
        print("3. Salir del programa")

        opcion = obtener_opcion_valida("Seleccione una opción: ", [1, 2, 3])

        if opcion == 1:
            while True:
                limpiar_pantalla()
                print("===== Configuración Campers =====")
                print("1. Crear Camper")
                print("2. Listar Campers")
                print("3. Modificar Camper")
                print("4. Crear Trainer")
                print("5. Modificar Trainer")
                print("6. Eliminar Camper")
                print("7. Eliminar Trainer")
                print("8. Volver al Menú Principal")

                sub_opcion = obtener_opcion_valida("Seleccione una opción: ", [1, 2, 3, 4, 5, 6, 7, 8])

                if sub_opcion == 1:
                    crear_camper(datos)
                elif sub_opcion == 2:
                    listar_campers(datos)
                elif sub_opcion == 3:
                    modificar_camper(datos)
                elif sub_opcion == 4:
                    crear_trainer(datos)
                elif sub_opcion == 5:
                    modificar_trainer(datos)
                elif sub_opcion == 6:
                    eliminar_camper(datos)
                elif sub_opcion == 7:
                    eliminar_trainer(datos)
                elif sub_opcion == 8:
                    break
        elif opcion == 2:
            while True:
                limpiar_pantalla()
                print("===== Configuración Trainers =====")
                print("1. Ver Horario")
                print("2. Salir")

                sub_opcion = obtener_opcion_valida("Seleccione una opción: ", [1, 2])

                if sub_opcion == 1:
                    ver_horario(datos)
                elif sub_opcion == 2:
                    break
        elif opcion == 3:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    datos = cargar_datos()
    menu_coordinador(datos)