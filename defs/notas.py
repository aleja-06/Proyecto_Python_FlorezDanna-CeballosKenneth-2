from defs.funciones import *
from defs.funciones_campers import *

import json
import os

# Ruta al archivo JSON
json_path = os.path.join("data", "campers.json")

def cargar_campers():
    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            campers = json.load(file)
    else:
        campers = []
    return campers

def guardar_campers(campers):
    with open(json_path, 'w') as file:
        json.dump(campers, file, indent=2)

def evaluar_camper(camper_id):
    campers = cargar_campers()
    camper_encontrado = None

    for camper in campers:
        if camper["ID"] == camper_id:
            camper_encontrado = camper
            break

    if not camper_encontrado:
        print(f"No se encontró un camper con ID {camper_id}.")
        return

    nota_teorica = float(input("Ingrese la nota teórica del camper (0-100): "))
    nota_practica = float(input("Ingrese la nota práctica del camper (0-100): "))
    nota_trabajos = float(input("Ingrese la nota de los trabajos del camper (0-100): "))

    promedio = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_trabajos * 0.1)

    aprobado = promedio >= 60

    camper_encontrado["nota_teorica"] = nota_teorica
    camper_encontrado["nota_practica"] = nota_practica
    camper_encontrado["nota_trabajos"] = nota_trabajos
    camper_encontrado["promedio"] = promedio
    camper_encontrado["aprobado"] = aprobado

    guardar_campers(campers)

    print(f"\nEl camper con ID {camper_id} ha sido evaluado. Promedio: {promedio:.2f}. {'Aprobado' if aprobado else 'Reprobado'}")