from defs.funciones import *
from menus.all_menu import *
from defs.funciones_campers import *
from defs.funciones_trainers import *
from defs.notas import *

def menu_principal():
    print("--------Menu Principal--------")
    print("1. Coordinador")
    print("2. Trainer")
    print("3. Salir")


while True:
    clear_screen()
    menu_principal()
    opc=verify_opc("Digite una opción: ",1,3)

    if opc==1:
        clear_screen()
        menu_coordinador()
        ops=verify_opc("Digite una opcion: ",1,10)
        if ops==1:
            clear_screen()
            crear_camper()
        if ops==2:
            clear_screen()
            listar_campers()
        if ops==3:
            clear_screen()
            modificar_camper()
        if ops==4:
            clear_screen()
            crear_trainer()
        if ops==5:
            clear_screen()
            listar_trainers()
        if ops==6:
            clear_screen()
            modificar_trainer()
        if ops==7:
            clear_screen()
            eliminar_camper()
        if ops==8:
            clear_screen()
            eliminar_trainer()
        if ops==9:
            clear_screen()
            camper_id = input("Ingrese el ID del camper: ")
        if ops==10:
            clear_screen()
            menu_principal()
        
    if opc==2:
        clear_screen()
        menu_trainer()
        ops=verify_opc("Digite una opcion: ",1,2)
        if ops ==1:
            clear_screen()
            ver_horario()
        if ops==2:
            clear_screen()
            menu_principal()
    if opc==3:
        clear_screen()
        cerrar_programa()
        break