from menu.menus import *
from mas.funciones import *
from mas.mas_camper import *


def coordinador():
    clear_screen()
    opc=menu_coordinador()
    if opc==1:
        registrar_camper()


def salir_programa():
    clear_screen()
    print("----------Cerrando Sesión----------")
    print("")
    print("")
    print("Gracias por usar nuestro programa :3")
    print("")
    print("")
    print("------------------------------------")



def horario_trainer():
    clear_screen()
    print("----------Menu Trainer----------")
    print("")
    print("Aqui se mostraran todos los horarios dependiendo del trainer")
    print("")
    print("El usuario podra ingresar su nombre y se vera su horario")
    print("O estoy pensando si pedirle su ID xd")


while True:
    clear_screen()
    opc=menu_roles()
    if opc==1:
        coordinador()
    if opc==2:
        horario_trainer()
    if opc==3:
        salir_programa()
        break
