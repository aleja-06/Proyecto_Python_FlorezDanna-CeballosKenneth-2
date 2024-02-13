from mas.funciones import *
from datas.funciones_data import *

#Aqui van las funciones de los campers

def registrar_camper(datos):
    clear_screen()
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