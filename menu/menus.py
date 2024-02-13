import os
from mas.funciones import *


def menu_roles():
    clear_screen()
    print("----------Menú De Roles----------")
    print("1. Coordinador")
    print("2. Trainer")
    print("3. Salir")    
    opc=verify_opc("Porfavor digite su opcion: ",1,3)
    return opc
      
def menu_coordinador():
    print("===== Menú Coordinador =====")
    print("1. Crear Camper")
    print("2. Listar Campers")
    print("3. Modificar Camper")
    print("4. Crear Trainer")
    print("5. Modificar Trainer")
    print("6. Eliminar Camper")
    print("7. Eliminar Trainer")
    print("8. Volver al Menú Principal") 
      
      
def menu_campers():
    print("----------Menú Campers----------")
    print("1. Crear camper")
    print("2. Listar camper")
    print("3. Ingresar nota de los modulos")
    print("4. Ingresar nota de la prueba inicial")
    print("5. Definir ruta del camper")
    print("6. Modificar campers")
    print("7. Salir")
    opc=verify_opc("Porfavor digite su opcion: ",1,7)
    return opc
  
def menu_rutas():
    print("----------- Menú Rutas -----------")
    print("1. Creación de rutas de entrenamiento")
    print("2. Listar ruta de entrenamiento")
    print("3. Borrar ruta de entrenamiento")
    print("4. Salir")
    opc=verify_opc("Porfavor digite su opcion: ",1,4)
    return opc
    
def menu_ruta():
    print("----------- Menú De Seleccion De Ruta -----------")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    print("4. Salir")
    opc=verify_opc("Porfavor digite su opcion: ",1,4)
    return opc

def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Crear trainers")
    print("2. Buscar trainers")
    print("3. Modificar trainers")
    print("4. Listar trainers")
    print("5. Agregar trainer a una ruta")
    print("6. Agregar trainer a una area")
    print("7. Salir")
    opc=verify_opc("Porfavor digite su opcion: ",1,7)
    return opc

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Crear Matriculas")
    print("2. Listar Matriculas")
    print("3. Modificar Matriculas")
    print("4. Salir")
    opc=verify_opc("Porfavor digite su opcion: ",1,4)
    return opc

def menu_aulas():
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Agregar campers a aulas")
    print("3. Listar Aulas activas")
    print("4. Modificar Aulas")
    print("5. Salir")
    opc=verify_opc("Porfavor digite su opcion: ",1,5)
    return opc

def menu_reportes():
    print("----------- Menú Reportes-----------")   
    print("1. Listar los campers inscritos")
    print("2. Listar los campers que aprobaron el examen inicial")
    print("3. Listar los entrenadores trabajando")
    print("4. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos")
    print("5. Salir")

    opc=verify_opc("Porfavor digite su opcion: ",1,5)
    return opc

def cerrar_sesion():
        print("-----------------------Cerrando Sesión-----------------------")
        print("")
        print("")
        print("Gracias por usar nuestro programa :3")
        print("")
        print("")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣤⣼⣿⣿⣿⣿⣿⣿⣷⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⠛⢻⠉⡉⠍⠁⠁⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⢠⢀⡼⡄⠃⠤⠀⠀⠀⠀⠀⡐⠸⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢰⣸⡎⣀⣷⣤⣶⣶⣶⣦⡀⠀⠈⠓⢿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣇⣤⣯⣿⣿⣿⣿⣿⣿⣿⣭⣯⡆⠀⠀⠘⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣻⣿⣿⣼⠀⢹⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢘⣿⠙⠡⢽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣛⣿⣯⠏⠀⢀⣿⣿⣿⣯⣠⡀⠀⠀⠀⢀⣾⡏⠒⢻⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⢘⣏⣺⣤⣬⣭⣼⣿⣿⣯⡉⢻⣦⣌⣦⣾⣿⣿⡚⠾⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⡼⣿⣿⢼⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⣿⢿⡟⢳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣧⡞⣻⣩⣽⡽⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣇⣬⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡛⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡟⠻⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⠓⠲⠤⢤⣄⡀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠈⣿⡏⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢯⡁⠀⠀⠀⠉⠹⠶⢤⣀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⢀⠹⣿⡆⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣤⣄⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⢩⠀⢸⡄⢹⣿⣦⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣤⡄⠀⢀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⡀⣀⣰⣿⠀⠄⠹⣾⣿⣿⡿⣿⠀⢠⣤⣀⣴⣤⣤⡴⠶⠶⠿⠿⠛⠛⠋⠉⠉⣠⣿")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⢀⡱⠏⠉⡟⠃⠀⠀⠀⢸⣿⣿⠇⣿⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⢋⣡⣶⣿⣂⡼⠁⠉⠙⠋⠙⠿⠟⣢⣄⢿⡟⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀")
        print("⠀⠀⠀⢀⣠⠴⠚⠉⠉⠀⠀⠀⠀⠀⣸⡿⠟⠀⠀⠀⠀⠀⠀⠲⣾⡛⣿⣬⡄⠀⠀⠁⠠⣤⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⡟⣿⡟⠀⠀⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀")
        print("⠞⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡀⡀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠁⠆⠀⠀⠀")
        print("--------------------------------------------------------------")
###################################################################################################var(--black)

#MENUS REALES 

def modificar_trainer(datos):
    clear_screen()
    print("==== Modificar Trainer ====")
    id_trainer = input("Ingresa la ID del Trainer que deseas modificar: ")
    encontrado = False
    for trainer in datos["trainers"]:
        if trainer["id"] == id_trainer:
            print(f"Datos actuales de {trainer['nombre']} {trainer['apellido']}:")
            print(f"Nombre: {trainer['nombre']}")
            print(f"Apellido: {trainer['apellido']}")
            print(f"Horario: {trainer['horario']}")
            print("\nIngrese los nuevos datos:")
            trainer["nombre"] = input("Nombre: ")
            trainer["apellido"] = input("Apellido: ")
            trainer["horario"] = input("Horario: ")
            encontrado = True
            guardar_datos(datos)
            print("Trainer modificado exitosamente.")
            break
    if not encontrado:
        print("No se encontró un Trainer con esa ID.")
    input("Presiona Enter para volver al menú.")
    
    
def eliminar_camper(datos):
    clear_screen()
    print("==== Eliminar Camper ====")
    id_camper = input("Ingresa la ID del Camper que deseas eliminar: ")
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            datos["campers"].remove(camper)
            guardar_datos(datos)
            print("Camper eliminado exitosamente.")
            input("Presiona Enter para volver al menú.")
            return
    print("No se encontró un Camper con esa ID.")
    input("Presiona Enter para volver al menú.")

def eliminar_trainer(datos):
    clear_screen()
    print("==== Eliminar Trainer ====")
    id_trainer = input("Ingresa la ID del Trainer que deseas eliminar: ")
    for trainer in datos["trainers"]:
        if trainer["id"] == id_trainer:
            datos["trainers"].remove(trainer)
            guardar_datos(datos)
            print("Trainer eliminado exitosamente.")
            input("Presiona Enter para volver al menú.")
            return
    print("No se encontró un Trainer con esa ID.")
    input("Presiona Enter para volver al menú.")
    
def listar_campers(datos):
    clear_screen()
    print("==== Listar Campers ====")
    if datos["campers"]:
        for camper in datos["campers"]:
            print(f"ID: {camper['id']} - {camper['nombre']} {camper['apellido']}")
    else:
        print("No hay campers registrados.")
    input("Presiona Enter para volver al menú.")
    
    
def modificar_camper(datos):
    clear_screen()
    print("==== Modificar Camper ====")
    id_camper = input("Ingresa la ID del Camper que deseas modificar: ")
    encontrado = False
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            print(f"Datos actuales de {camper['nombre']} {camper['apellido']}:")
            print(f"Nombre: {camper['nombre']}")
            print(f"Apellido: {camper['apellido']}")
            print(f"Dirección: {camper['direccion']}")
            print(f"Acudiente: {camper['acudiente']}")
            print(f"Teléfono Celular: {camper['telefono_celular']}")
            print(f"Teléfono Fijo: {camper['telefono_fijo']}")
            print("\nIngrese los nuevos datos:")
            camper["nombre"] = input("Nombre: ")
            camper["apellido"] = input("Apellido: ")
            camper["direccion"] = input("Dirección: ")
            camper["acudiente"] = input("Acudiente: ")
            camper["telefono_celular"] = input("Teléfono Celular: ")
            camper["telefono_fijo"] = input("Teléfono Fijo: ")
            encontrado = True
            guardar_datos(datos)
            print("Camper modificado exitosamente.")
            break
    if not encontrado:
        print("No se encontró un Camper con esa ID.")
    input("Presiona Enter para volver al menú.")
    
def crear_trainer(datos):
    clear_screen()
    print("==== Crear Trainer ====")
    nombre = input("Nombre del Trainer: ")
    apellido = input("Apellido del Trainer: ")
    horario = input("Horario del Trainer (mañana/tarde): ")
    id_trainer = input("ID del Trainer: ")

    nuevo_trainer = {
        "nombre": nombre,
        "apellido": apellido,
        "horario": horario,
        "id": id_trainer
    }

    datos["trainers"].append(nuevo_trainer)
    guardar_datos(datos)
    print("Trainer creado exitosamente.")
    input("Presiona Enter para volver al menú.")

def ver_horario(datos):
    clear_screen()
    print("==== Ver Horario del Trainer ====")
    id_trainer = input("Ingresa la ID del Trainer: ")
    encontrado = False
    for trainer in datos["trainers"]:
        if trainer["id"] == id_trainer:
            print(f"Horario de {trainer['nombre']} {trainer['apellido']}: {trainer['horario']}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un Trainer con esa ID.")
    input("Presiona Enter para volver al menú.")
    
def menu_trainer(datos):
    print("===== Configuración Trainers =====")
    print("1. Ver Horario")
    print("2. Salir")