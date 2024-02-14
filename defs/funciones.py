import os
import json

#Funciones escenciales
def guardar_datos(carpeta, archivo, datos):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    with open(os.path.join(carpeta, archivo), 'w') as file:
        json.dump(datos, file, indent=4)  # Puedes ajustar el valor de indent según tus preferencias


def cargar_datos(carpeta, archivo):
    ruta = os.path.join(carpeta, archivo)
    if os.path.exists(ruta):
        with open(ruta, 'r') as file:
            return json.load(file)
    return []

#
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def verify_opc(enunciado, bajo, top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Opcion no esta en el intervalo de ({bajo}-{top})")
        except ValueError:
            print("Por favor, digite un numero valido")
