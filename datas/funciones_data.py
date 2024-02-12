import json
import os
from menu.menus import *

def json_guardar_campers():
    try:
        with open(os.path.join("base_datos", "campers.json"), 'r') as archivo_json:
            lista_campers = json.load(archivo_json)
        print("La lista de campers ha sido cargada")
        return lista_campers
    except FileNotFoundError:
        return []
    
    
lista_campers=json_guardar_campers

def json_guardar():
    try:
        with open(os.path.join("base_datos", "campers.json"), 'w') as archivo_json: 
            json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
    