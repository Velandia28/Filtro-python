print ("HOLA BIENVENIDO A CAMPUSLANDS")
from mod_registrar import *
import json
while True:

    menu_principal=("1. Regristrar nuevos Campers","2. Rutas","3. Areas de Entrenamiento","4. Coordinacion Academica","5. Trainers","6. SALIR")
    for i in menu_principal:
        print(i)
    opc = (int(input("Ingrese el numero del menu al qu1e desea ingresar: ")))
    if opc == len(menu_principal):
        print("SALIENDO.....")
        break
    elif opc == 1:
        print("********************************************************")
        print("Haz seleccionado la opcion de Registrar un nuevo camper ")
        registrar_camper()
        print("********************************************************")
        


