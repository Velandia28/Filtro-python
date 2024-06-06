import json

ruta_archivo = "proyecto filtro python/campers.json"
datos = {
    "Doc": "",
    "Nombres": "",
    "Apellidos": "",
    "Direccion": "",
    "Acudiente": "",
    "Celular": "",
    "Estado": "proceso de ingreso",
    "Ruta Asignada": "",
    "Riesgo": "",
    "Aula": "",
    "Trainer":"",
    "Horario":""
}

def mostrar_menu(menu):
    for i in menu:
        print(i)

def cargar_datos():
    try:
        with open(ruta_archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo no existe")
        print("----------------")
        print("¡¡¡Ceando el Archivo !!!")
        return []

def guardar_datos(data):
    with open(ruta_archivo, "w") as file:
        json.dump(data, file, indent=4)

def menu_principal():
    print("                        ")
    print("BIENVENIDO A CAMPUSLANDS")
    print("                        ")
    print("Con qué rol va a ingresar a Campuslands")
    print("                                         ")

    menu_principal = ("1. Coordinador", "2. Trainer", "3. Camper", "4. SALIR ")

    while True:
        mostrar_menu(menu_principal)
        try:
            print("     ")
            opc = int(input("Ingrese el número del menú al que desea ingresar: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        if opc == len(menu_principal):
            print("                        ")
            print("SALIENDO.....")
            print("*****************************")
            break
        elif opc == 1:
            menu_coordinador()
        elif opc == 2:
            menu_trainer()
        elif opc == 3:
            print("                            ")
            print(" BIENVENIDO CAMPER ")
            # Aquí puedes añadir las opciones del Camper si es necesario.
        else:
            print("Opción no válida, por favor intente nuevamente.")

def menu_coordinador():
    print("                         ")
    print("BIENVENIDO COORDINADOR")
    print ("                       ")
    print("Escoja la opción que va a realizar")
    menu_cor = ("1. registrar camper", "2. registrar notas","3. Ingresar matricula ","4. Asignar area de entrenamiento ","5. estado de riesgo ", "6. SALIR.. ","7. Volver ")
    while True:
        mostrar_menu(menu_cor)
        try:
            opci = int(input("Ingrese el número del menú al que desea ingresar: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        if opci == len(menu_cor) - 1:
            print("SALIENDO.....")
            break
        elif opci == 7:
            return
        elif opci == 1:
            registrar_camper()
        elif opci == 2:
            registrar_notas()
        elif opci == 3:
            ingresar_matricula()
        elif opci == 4:
            asignar_area_entrenamiento()
        elif opci == 5:
            estado_riesgo()    
        else:
            print("Opción no válida, por favor intente nuevamente.")

def menu_trainer():
    print("                            ")
    print(" BIENVENIDO TRAINER ")
    print("Escoja la opción que va a realizar")

    menu_trainer = ("1. Asignar ruta","2. Asignar Horario ","3. SALIR ","4. Volver")

    while True:
        mostrar_menu(menu_trainer)
        try:
            opcio = int(input("Ingrese el número del menú al que desea ingresar: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        if opcio == len(menu_trainer) - 1:
            print("SALIENDO.....")
            break
        elif opcio == 4:
            return
        elif opcio == 1:
            asignar_ruta()
        elif opcio == 2:
            asignar_horario()
        else:
            print("Opción no válida, por favor intente nuevamente.")

def registrar_camper():
    data = cargar_datos()
    print("****************************************************")
    datos["Doc"] = input("Ingrese su Número de Documento: ")
    datos["Nombres"] = input("Ingrese sus Nombres: ")
    datos["Apellidos"] = input("Ingrese sus Apellidos: ")
    datos["Direccion"] = input("Ingrese su Dirección de residencia: ")
    datos["Acudiente"] = input("Ingrese los Datos de su Acudiente: ")
    datos["Celular"] = input("Ingrese su Número de celular: ")
    data.append(datos)
    guardar_datos(data)
    print("********************************************************")
    print("Se ha registrado correctamente")
    print("********************************************************")

def registrar_notas():
    doc = input("Ingrese el documento para ingresar notas: ")
    data = cargar_datos()
    camper = next((item for item in data if item["Doc"] == doc), None)
    if camper:
        try:
            nota_teo = int(input("Digite la nota de la prueba teórica: "))
            nota_pract = int(input("Digite la nota de la prueba práctica: "))
        except ValueError:
            print("Error de digitación, favor ingresar UNICAMENTE NÚMEROS")
            nota_teo, nota_pract = 0, 0
        global prom
        prom = (nota_pract + nota_teo) / 2
        if prom >= 60:
            camper["Estado"] = "Aprobado"
            guardar_datos(data)
            print("********************************************************")
            print("Se ha registrado correctamente")
            print("********************************************************")
        else:
            print("El promedio es menor a 60. No se puede aprobar.")
    else:
        print("No se encontró un camper con ese documento.")

def ingresar_matricula():
    doc = input("Ingrese el documento para modificar ruta: ")
    data = cargar_datos()
    camper = next((item for item in data if item["Doc"] == doc), None)
    if camper:
        ruta = input("Ingrese el nombre de la ruta asignada (Java, NetCore, NodeJs): ")
        camper["Ruta Asignada"] = ruta
        guardar_datos(data)
        if camper["Ruta Asignada"].lower() == "java":
            print("****************************************************************")
            print("Contiene los siguientes módulos: ", "Fundamentos de programación", "Programación Web", "Programación formal", "Bases de datos", "Backend")
        elif camper["Ruta Asignada"].lower() == "netcore":
            print("****************************************************************")
            print("Contiene los siguientes módulos: ", "Fundamentos de programación", "Programación Web", "Programación formal", "Bases de datos", "Backend")
        elif camper["Ruta Asignada"].lower() == "nodejs":
            print("****************************************************************")
            print("Contiene los siguientes módulos: ", "Fundamentos de programación", "Programación Web", "Programación formal", "Bases de datos", "Backend")
    print("********************************************************")
    print("Se ha registrado correctamente")
    print("********************************************************")

def asignar_area_entrenamiento():
    doc = input("Ingrese el documento para asignar el aula: ")
    data = cargar_datos()
    camper = next((item for item in data if item["Doc"] == doc), None)
    if camper:
        if camper["Ruta Asignada"].lower() == "java":
            camper["Aula"] = "Sputnik"
        elif camper["Ruta Asignada"].lower() == "netcore":
            camper["Aula"] = "Artemis"
        elif camper["Ruta Asignada"].lower() == "nodejs":
            camper["Aula"] = "Apolo"
            aula=aula+1

        guardar_datos(data)
        print("********************************************************")
        print("Se ha registrado correctamente")
        print("********************************************************")

def asignar_ruta():
    doc = input("Ingrese el documento para asignar un trainer según la ruta a desarrollar: ")
    data = cargar_datos()
    camper = next((item for item in data if item["Doc"] == doc), None)
    if camper:
        print(datos["Ruta Asignada"])
        trainer = input("Ingrese el nombre del Trainer que va a desarrollar su ruta asignada: ")
        camper["Trainer"] = trainer
        guardar_datos(data)
        print("********************************************************")
        print("Se ha registrado correctamente")
        print("********************************************************")
       
def asignar_horario():
    doc = input("Ingrese el documento para asignar un horario: ")
    print("Los horarios de las clases inician cada 4 horas y los horarios disponibles son", "(Lunes - Viernes)", "(6.00 am - 10.00 am)", "(10.00 am - 2.00 pm)", "(2.00 pm - 6.00 pm)", "(6.00 pm - 10.00 pm)")
    data = cargar_datos()
    camper = next((item for item in data if item["Doc"] == doc), None)
    if camper:
        print(datos["Ruta Asignada"])
        horario = input("Ingrese el horario que más se ajusta a usted para desarrollar la ruta programada: ")
        camper["Horario"] = horario
        guardar_datos(data)
        print("********************************************************")
        print("Se ha registrado correctamente")
        print("********************************************************")
        
def estado_riesgo():
    doc = input("Ingrese el documento para cambiar su estado de riesgo segun su nota : ")
    data=cargar_datos()
    camper = next((item for item in data if item["Doc"] == doc), None)
    if camper:
        # print(datos["Ruta Asignada"])
        if datos["Estado"]=="proceso de ingreso":      
            camper["Riesgo"] = "Todavia no es un CAMPER OFICIAL"
        elif datos["Estado"] == "Aprobado" and prom < 60:
            camper["Riesgo"] = "Riesgo alto segun el promedio que tiene"
        elif datos["Estado"] == "Aprobado"  and prom >60 and  prom <90:
            camper["Riesgo"] = "Riesgo medio segun el promedio que tiene"
        elif datos["Estado"] == "Aprobado"  and prom >= 90:
            camper["Riesgo"] = "Riesgo bajo  segun el promedio que tiene"
    guardar_datos(data)
    print("********************************************************")
    print("Se ha registrado correctamente")
    print("********************************************************")       
        
menu_principal()