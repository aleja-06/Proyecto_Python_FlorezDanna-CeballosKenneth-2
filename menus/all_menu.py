from defs.funciones import *

def menu_coordinador():
    print("-------Menú Coordinador-------")
    print("1. Crear Camper")
    print("2. Listar Camper")
    print("3. Modificar Camper")
    print("4. Crear Trainer")
    print("5. Listar Trainer")
    print("6. Modificar Trainer")
    print("7. Eliminar Camper")
    print("8. Eliminar Trainer")
    print("9. Volver")

def menu_trainer():
    print("-------Menú Trainer-------")
    print("1. Ver horario asignado")
    print("2. Salir al menu principal")

def cerrar_programa():
        print("----------------Cerrando Programa----------------")
        print("")
        print("")
        print("Gracias por usar nuestro programa :3")
        print("")
        print("")
        print("-------------------------------------------------")

def crear_camper():
    print("----------Crear Camper----------")
    print("")
    nombre = input("Ingrese el primer nombre del camper: ")
    clear_screen()
    print("----------Crear Camper----------")
    print("")
    apellido = input("Ingrese el primer apellido del camper: ")
    clear_screen()
    print("----------Crear Camper----------")
    print("")
    id_camper = input("Digite el ID del camper: ")
    clear_screen()
    print("----------Crear Camper----------")
    print("")
    direccion = input("Ingrese la direccion del camper: ")
    clear_screen()
    print("----------Crear Camper----------")
    print("")
    acudiente = input("Ingrese el nombre del acudiente del camper: ")
    clear_screen()
    print("----------Crear Camper----------")
    print("")
    tlfcc = input("Digite el numero celular del camper: ")
    clear_screen()
    print("----------Crear Camper----------")
    print("")
    tlffc = input("Digite el numero telefonico del camper: ")
    clear_screen()
    print("----------Crear Camper----------")
    print("")
    print("¿En que Estado se encuentra el camper? ")
    print("-En proceso de ingreso")
    print("-Inscrito")
    print("-Aprobando")
    print("-Cursando")
    print("-Graduado")
    print("-Expulsado")
    print("-Retirado")
    estado = input("Estado: ")
    clear_screen()

    campers = cargar_datos("datas", "campers.json")
    campers.append({
        "nombre": nombre,
        "apellido": apellido,
        "id_camper": id_camper,
        "direccion": direccion,
        "acudiente": acudiente,
        "tlfcc": tlfcc,
        "tlffc": tlffc,
        "estado": estado
    })
    guardar_datos("datas", "campers.json", campers)
    print("----------Crear Camper----------")
    print("")
    input("Camper creado correctamente ;)...")

def listar_campers():
    campers = cargar_datos("datas", "campers.json")
    if campers:
        print("\n--------Campers--------")
        for camper in campers:
            print(f"Nombre: {camper['nombre']}")
            print(f"Apellido: {camper['apellido']}")
            print(f"ID del camper: {camper['id_camper']}")
            print(f"Direccion del camper: {camper['direccion']}")
            print(f"Acudiente del camper: {camper['acudiente']}")
            print(f"Telefono celular del camper: {camper['tlfcc']}")
            print(f"Telefono fijo del camper: {camper['tlffc']}")
            print(f"Estado del camper: {camper['estado']}")
            print("-------------------------------")
        print()
    else:
        print("No hay campers registrados.")
    input("Presione Enter para volver al menú.")

def modificar_camper():
    campers = cargar_datos("datas", "campers.json")
    if campers:
        id_modificar = input("Ingrese la ID del camper a modificar: ")
        for camper in campers:
            if camper["id_camper"] == id_modificar:
                print("Datos actuales del camper:")
                print(f"Nombre: {camper['nombre']}")
                print(f"Apellido: {camper['apellido']}")
                print(f"ID del camper: {camper['id_camper']}")
                print(f"Direccion del camper: {camper['direccion']}")
                print(f"Acudiente del camper: {camper['acudiente']}")
                print(f"Telefono celular del camper: {camper['tlfcc']}")
                print(f"Telefono fijo del camper: {camper['tlffc']}")
                print(f"Estado del camper: {camper['estado']}")
                print("-------------------------")
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_apellido = input("Ingrese el nuevo apellido: ")
                nueva_direccion = input("Ingrese la nueva direccion del camper: ")
                nuevo_acudiente = input("Ingrese el nuevo acudiente del camper: ")
                nuevo_tlfcc = input("Ingrese el nuevo telefono celular del camper: ")
                nuevo_tlffc = input("Ingrese el nuevo telefono fijo del camper: ")
                nuevo_estado = input("Ingrese el nuevo estado del camper: ")

                camper["nombre"] = nuevo_nombre
                camper["apellido"] = nuevo_apellido
                camper["direccion"] = nueva_direccion
                camper["acudiente"] = nuevo_acudiente
                camper["tlfcc"] = nuevo_tlfcc
                camper["tlffc"] = nuevo_tlffc
                camper["estado"] = nuevo_estado

                guardar_datos("datas", "campers.json", campers)
                print("Camper modificado con éxito.")
                input("Presione Enter para volver al menú.")
                return
        print("Camper no encontrado :c.")
    else:
        print("No hay campers registrados.")
    input("Presione Enter para volver al menú.")

def crear_trainer():
    print("----------Crear Trainer----------")
    print("")
    nombre=input("Escriba el nombre del trainer: ")
    print("")
    clear_screen()
    print("----------Crear Trainer----------")
    print("")
    apellido=input("Escriba el apellido del trainer: ")
    clear_screen()
    print("----------Crear Trainer----------")
    print("")
    print("Escriba su jornada, mañana/tarde: ")
    clear_screen()
    print("")
    print("----------Crear Trainer----------")
    print("")
    id=input("Digite el ID del trainer: ")

def listar_trainer():
    trainers=