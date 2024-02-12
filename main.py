from menu.menus import *
from mas.funciones import *
from mas.mas_camper import *


def coordinador():
    clear_screen()
    opc=menu_coordinador()
    if opc==1:
        registrar_camper()
        print("Vamo mesi")







while True:
    clear_screen()
    opc=menu_roles()
    if opc==1:
        coordinador()
    if opc==2:
        print("Aqui deben estar los horarios del trainer xd")
        break
    if opc==3:
        print("Gracias por usar nuestro programa :3")
        break