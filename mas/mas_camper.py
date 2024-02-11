from mas.funciones import *

def registrar_camper():
    clear_screen()
    print("Sistema de registro campers")
    
    nombre=input("Ingresa el nombre del camper: ")
    apellido=input("Ingrese el apellido del camper: ")
    id=int(input("Ingrese el documento del camper: "))
    direccion=input("Ingrese la direccion del camper: ")
    acudiente = input("Ingrese el acudiente del camper: ")
    telefono_celular = input("Ingrese el numero celular del camper: ")
    telefono_fijo = input("Ingrese el numero fijo del camper: ")  

    camper={
        'nombre': nombre,
        'apellido': apellido,
        'identificacion': id,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefono_celular': telefono_celular,
        'telefono_fijo': telefono_fijo,
        'estado': "Inscrito"
    }