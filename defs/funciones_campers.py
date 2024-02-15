from defs.funciones import *


def crear_camper():
    clear_screen()
    print("=== Crear Camper ===")
    id_camper = input("Número de Identificación: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    acudiente = input("Acudiente: ")
    telefono_celular = input("Teléfono Celular: ")
    telefono_fijo = input("Teléfono Fijo: ")
    estado = input("Estado (En proceso de ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado): ")

    nuevo_camper = {
        "ID": id_camper,
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Dirección": direccion,
        "Acudiente": acudiente,
        "Teléfono Celular": telefono_celular,
        "Teléfono Fijo": telefono_fijo,
        "Estado": estado
    }

    try:
        os.makedirs("data", exist_ok=True)  
        with open("data/campers.json", "r") as file:
            campers = json.load(file)
    except FileNotFoundError:
        campers = []

    campers.append(nuevo_camper)

    with open("data/campers.json", "w") as file:
        json.dump(campers, file, indent=2)

    input("Camper creado. Presione Enter para continuar.")

def listar_campers():
    clear_screen()
    print("=== Listar Campers ===")
    try:
        with open("data/campers.json", "r") as file:
            campers = json.load(file)
            if not campers:
                print("No hay campers registrados.")
            else:
                for camper in campers:
                    print("\nID:", camper["ID"])
                    print("Nombres:", camper["Nombres"])
                    print("Apellidos:", camper["Apellidos"])
                    print("Dirección:", camper["Dirección"])
                    print("Acudiente:", camper["Acudiente"])
                    print("Teléfono Celular:", camper["Teléfono Celular"])
                    print("Teléfono Fijo:", camper["Teléfono Fijo"])
                    print("Estado:", camper["Estado"])
                    print("=" * 40)
    except FileNotFoundError:
        print("No hay campers registrados.")

    input("Presione Enter para continuar.")

def eliminar_camper():
    clear_screen()
    print("=== Eliminar Camper ===")
    id_camper = input("Ingrese la ID del Camper a eliminar: ")

    try:
        with open("data/campers.json", "r") as file:
            campers = json.load(file)
        
        for camper in campers:
            if camper["ID"] == id_camper:
                print("Datos del Camper a eliminar:")
                print("\nID:", camper["ID"])
                print("Nombres:", camper["Nombres"])
                print("Apellidos:", camper["Apellidos"])
                print("Dirección:", camper["Dirección"])
                print("Acudiente:", camper["Acudiente"])
                print("Teléfono Celular:", camper["Teléfono Celular"])
                print("Teléfono Fijo:", camper["Teléfono Fijo"])
                print("Estado:", camper["Estado"])
                print("=" * 40)
                confirmacion = input("¿Está seguro de que desea eliminar este Camper? (s/n): ").lower()
                if confirmacion == "s":
                    campers.remove(camper)
                    with open("data/campers.json", "w") as write_file:
                        json.dump(campers, write_file, indent=2)
                        print("Camper eliminado correctamente.")
                        input("Presione Enter para continuar.")
                    return
                else:
                    print("Eliminación cancelada.")
                    input("Presione Enter para continuar.")
                    return
        
        print("Camper no encontrado.")
        input("Presione Enter para continuar.")
    except FileNotFoundError:
        print("No hay campers registrados.")
        input("Presione Enter para continuar.")
        
def modificar_camper():
    clear_screen()
    print("=== Modificar Camper ===")
    id_camper = input("Ingrese la ID del Camper a modificar: ")

    try:
        with open("data/campers.json", "r") as file:
            campers = json.load(file)
        
        for camper in campers:
            if camper["ID"] == id_camper:
                print("Datos actuales del Camper:")
                print("\nID:", camper["ID"])
                print("Nombres:", camper["Nombres"])
                print("Apellidos:", camper["Apellidos"])
                print("Dirección:", camper["Dirección"])
                print("Acudiente:", camper["Acudiente"])
                print("Teléfono Celular:", camper["Teléfono Celular"])
                print("Teléfono Fijo:", camper["Teléfono Fijo"])
                print("Estado:", camper["Estado"])
                print("=" * 40)

                campo_modificar = input("Ingrese el campo a modificar: ")
                nuevo_valor = input(f"Ingrese el nuevo valor para {campo_modificar}: ")
                
                if campo_modificar in camper:
                    camper[campo_modificar] = nuevo_valor
                    with open("data/campers.json", "w") as write_file:
                        json.dump(campers, write_file, indent=2)
                        print("Camper modificado correctamente.")
                        input("Presione Enter para continuar.")
                else:
                    print(f"Campo {campo_modificar} no válido.")
                    input("Presione Enter para continuar.")
                return
        
        print("Camper no encontrado.")
        input("Presione Enter para continuar.")
    except FileNotFoundError:
        print("No hay campers registrados.")
        input("Presione Enter para continuar.")
