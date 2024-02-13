from menu.menus import *
from mas.funciones import *
from mas.mas_camper import *
from datas.funciones_data import *

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
    print("----------Menú De Roles----------")
    print("1. Coordinador")
    print("2. Trainer")
    print("3. Salir")  
    opc=verify_opc("Digite una opcion: ",1,3)
    
    if opc==1:
        clear_screen()
        menu_coordinador()

        ops=verify_opc("Digite una opcion: ",1,8)
        if ops==1:
            registrar_camper()
        elif ops==2:
            listar_campers()            
        elif ops == 3:
            modificar_camper()
        elif ops == 4:
            crear_trainer()
        elif ops == 5:
            modificar_trainer()
        elif ops == 6:
            eliminar_camper()
        elif ops == 7:
            eliminar_trainer()
        elif ops == 8:
            break
    if opc==2:
        clear_screen()
        print("Aqui van los horarios :D")
        input("Presione Enter para volver ") #No se como hacer para que solo le de enter para que vuelva, lloro :c
                                             #Edit: Ya se como, solo era poner un input JAJAJSASKJDAKHSDA
    if opc==3:
        clear_screen()
        cerrar_sesion()
        break

