from defs.funciones import *

def crear_trainer():
    clear_screen()
    print("=== Crear Trainer ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    id_trainer = input("ID: ")
    jornada = input("Jornada (Mañana/Tarde): ")

    nuevo_trainer = {
        "Nombre": nombre,
        "Apellido": apellido,
        "ID": id_trainer,
        "Jornada": jornada
    }

    try:
        os.makedirs("data", exist_ok=True)  # Crear la carpeta "data" si no existe
        with open("data/trainers.json", "r") as file:
            trainers = json.load(file)
    except FileNotFoundError:
        trainers = []

    trainers.append(nuevo_trainer)

    with open("data/trainers.json", "w") as file:
        json.dump(trainers, file, indent=2)

    input("Trainer creado. Presione Enter para continuar.")

def listar_trainers():
    clear_screen()
    print("=== Listar Trainers ===")
    try:
        with open("data/trainers.json", "r") as file:
            trainers = json.load(file)
            if not trainers:
                print("No hay trainers registrados.")
            else:
                for trainer in trainers:
                    print("\nID:", trainer["ID"])
                    print("Nombre:", trainer["Nombre"])
                    print("Apellido:", trainer["Apellido"])
                    print("Jornada:", trainer["Jornada"])
                    print("=" * 40)
    except FileNotFoundError:
        print("No hay trainers registrados.")

    input("Presione Enter para continuar.")

def eliminar_trainer():
    clear_screen()
    print("=== Eliminar Trainer ===")
    id_trainer = input("Ingrese la ID del Trainer a eliminar: ")

    try:
        with open("data/trainers.json", "r") as file:
            trainers = json.load(file)
        
        for trainer in trainers:
            if trainer["ID"] == id_trainer:
                print("Datos del Trainer a eliminar:")
                print("\nID:", trainer["ID"])
                print("Nombre:", trainer["Nombre"])
                print("Apellido:", trainer["Apellido"])
                print("Jornada:", trainer["Jornada"])
                print("=" * 40)
                confirmacion = input("¿Está seguro de que desea eliminar este Trainer? (s/n): ").lower()
                if confirmacion == "s":
                    trainers.remove(trainer)
                    with open("data/trainers.json", "w") as write_file:
                        json.dump(trainers, write_file, indent=2)
                        print("Trainer eliminado correctamente.")
                        input("Presione Enter para continuar.")
                    return
                else:
                    print("Eliminación cancelada.")
                    input("Presione Enter para continuar.")
                    return
        
        print("Trainer no encontrado.")
        input("Presione Enter para continuar.")
    except FileNotFoundError:
        print("No hay trainers registrados.")
        input("Presione Enter para continuar.")

def modificar_trainer():
    clear_screen()
    print("=== Modificar Trainer ===")
    id_trainer = input("Ingrese la ID del Trainer a modificar: ")

    try:
        with open("data/trainers.json", "r") as file:
            trainers = json.load(file)
        
        for trainer in trainers:
            if trainer["ID"] == id_trainer:
                print("Datos actuales del Trainer:")
                print("\nID:", trainer["ID"])
                print("Nombre:", trainer["Nombre"])
                print("Apellido:", trainer["Apellido"])
                print("Jornada:", trainer["Jornada"])
                print("=" * 40)

                campo_modificar = input("Ingrese el campo a modificar: ")
                nuevo_valor = input(f"Ingrese el nuevo valor para {campo_modificar}: ")
                
                # Verificamos si el campo a modificar existe en el trainer
                if campo_modificar in trainer:
                    trainer[campo_modificar] = nuevo_valor
                    with open("data/trainers.json", "w") as write_file:
                        json.dump(trainers, write_file, indent=2)
                        print("Trainer modificado correctamente.")
                        input("Presione Enter para continuar.")
                else:
                    print(f"Campo {campo_modificar} no válido.")
                    input("Presione Enter para continuar.")
                return
        
        print("Trainer no encontrado.")
        input("Presione Enter para continuar.")
    except FileNotFoundError:
        print("No hay trainers registrados.")
        input("Presione Enter para continuar.")


def ver_horario():
    trainers = cargar_datos("datas", "trainers.json")
    
    if trainers:
        print("\n--------Horarios de Trainers--------")
        id_trainer = input("Ingrese la ID del trainer para ver su horario: ")

        trainer_encontrado = next((trainer for trainer in trainers if trainer["id"] == id_trainer), None)

        if trainer_encontrado:
            print(f"\nHorario del Trainer (ID: {id_trainer}):")
            print(f"Nombre: {trainer_encontrado['nombre']} {trainer_encontrado['apellido']}")
            print(f"Jornada: {trainer_encontrado['jornada']}")
        else:
            print(f"No se encontró ningún Trainer con la ID {id_trainer}.")
    else:
        print("No hay Trainers registrados.")

    input("Presione Enter para volver al menú.")