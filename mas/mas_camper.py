from mas.funciones import *
from datas.funciones_data import *

#Aqui van las funciones de los campers

def registrar_camper():
    clear_screen()
    print("Sistema de registro campers")
    
    nombre=input("Ingresa el nombre del camper: ")
    apellido=input("Ingrese el apellido del camper: ")
    id=int(input("Ingrese el documento del camper: "))
    direccion=input("Ingrese la direccion del camper: ")
    acudiente = input("Ingrese el acudiente del camper: ")
    tlf_celular = input("Ingrese el numero celular del camper: ")
    tlf_fijo = input("Ingrese el numero fijo del camper: ")  

    camper={
        'nombre': nombre,
        'apellido': apellido,
        'identificacion': id,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefono_celular': tlf_celular,
        'telefono_fijo': tlf_fijo,
        'estado': "Inscrito"
    }
    
    lista_campers.append(camper)
    print("Se ha creado el camper!")
    json_guardar()
    return camper