import json

#Aqui van las funciones de los campers

def cargar_camper():
    try:
        with open("campers.json","r") as file:
            campers=json.load(file)
    except FileNotFoundError:
        campers=[]
    return campers

def guardar_camper(campers):
    with open("campers.json","W") as file:
        json.dumb(campers, file, indent=2)

def registrar_camper():
    nombrec = input("Ingrese el nombre del camper: ")
    apellidoc=input("Ingrese el apellido del camper: ")
    id_camper=input("Ingrese el ID del camper: ")
    direccionc=input("Ingrese la dirección del camper: ")
    acudientec=input("Ingrese el nombre del acudiente del camper: ")
    tlfcc=input("Ingrese el numero de celular del camper: ")
    tlffc=input("Ingrese el numero telefonico del camper: ")
    
    nuevo_camper= {
        "Nombre":nombrec,
        "Apellido":apellidoc,
        "Id_camper":id_camper,
        "Dirección":direccionc,
        "Acudiente":acudientec,
        "Telefono celular":tlfcc,
        "Telefono fijo":tlffc
    }
    
    campers= cargar_camper()
    campers.append(nuevo_camper)
    guardar_camper(campers)
        
    print(f"!Camper '{nombrec}' creado y guardado exitosamente! :D")
    
def listar_campers():
    campers= cargar_camper()
    
    if not campers:
        print("No hay campers registrados.")
    else:
        print("Lista de Campers: ")
        for camper in campers:
            print()
            