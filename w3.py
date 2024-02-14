import json
import os

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def create_camper():
    # Función para crear un nuevo Camper
    camper = {}
    camper['nombre'] = input("Nombre: ")
    camper['apellido'] = input("Apellido: ")
    camper['id'] = input("ID: ")
    camper['direccion'] = input("Dirección: ")
    camper['acudiente'] = input("Acudiente: ")
    camper['telefono_celular'] = input("Teléfono Celular: ")
    camper['telefono_fijo'] = input("Teléfono Fijo: ")

    with open('campers.json', 'a') as file:
        json.dump(camper, file)
        file.write('\n')

def list_campers():
    # Función para listar todos los Campers
    with open('campers.json', 'r') as file:
        for line in file:
            camper = json.loads(line)
            print(camper)

def modify_camper():
    # Función para modificar un Camper
    id_to_modify = input("Ingrese la ID del Camper a modificar: ")

    with open('campers.json', 'r') as file:
        lines = file.readlines()

    with open('campers.json', 'w') as file:
        for line in lines:
            camper = json.loads(line)
            if camper['id'] == id_to_modify:
                # Modificar los datos
                camper['nombre'] = input("Nuevo nombre: ")
                camper['apellido'] = input("Nuevo apellido: ")
                camper['direccion'] = input("Nueva dirección: ")
                camper['acudiente'] = input("Nuevo acudiente: ")
                camper['telefono_celular'] = input("Nuevo teléfono celular: ")
                camper['telefono_fijo'] = input("Nuevo teléfono fijo: ")
            json.dump(camper, file)
            file.write('\n')

# Aquí seguirían las implementaciones de las demás funciones y menús

# Menú principal
while True:
    clear_screen()
    print("Menú Principal")
    print("1. Coordinador")
    print("2. Configuración Trainers")
    print("3. Salir")

    choice_main = input("Seleccione una opción: ")

    if choice_main == '1':
        # Menú Coordinador
        while True:
            clear_screen()
            print("Menú Coordinador")
            print("1. Configuración Campers")
            print("2. Configuración Trainers")
            print("3. Salir")

            choice_coordinator = input("Seleccione una opción: ")

            if choice_coordinator == '1':
                # Menú Configuración Campers
                while True:
                    clear_screen()
                    print("Configuración Campers")
                    print("1. Crear Camper")
                    print("2. Listar Campers")
                    print("3. Modificar Campers")
                    print("4. Crear Trainers")
                    print("5. Modificar Trainers")
                    print("6. Eliminar Camper")
                    print("7. Eliminar Trainer")
                    print("8. Volver al menú anterior")

                    choice_campers = input("Seleccione una opción: ")

                    if choice_campers == '1':
                        create_camper()
                    elif choice_campers == '2':
                        list_campers()
                    elif choice_campers == '3':
                        modify_camper()
                    # Aquí seguirían las implementaciones de las demás opciones de Configuración Campers
                    elif choice_campers == '8':
                        break
            elif choice_coordinator == '2':
                # Menú Configuración Trainers
                while True:
                    clear_screen()
                    print("Configuración Trainers")
                    print("1. Ver horario")
                    print("2. Salir")

                    choice_trainers = input("Seleccione una opción: ")

                    if choice_trainers == '1':
                        # Implementación de Ver horario
                        pass
                    elif choice_trainers == '2':
                        break
            elif choice_coordinator == '3':
                break
    elif choice_main == '2':
        # Menú Configuración Trainers
        while True:
            clear_screen()
            print("Configuración Trainers")
            print("1. Ver horario")
            print("2. Salir")

            choice_trainers = input("Seleccione una opción: ")

            if choice_trainers == '1':
                # Implementación de Ver horario
                pass
            elif choice_trainers == '2':
                break
    elif choice_main == '3':
        break
