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
print("                        ")
print("BIENVENIDO A CAMPUSLANDS")
print("                        ")
print("Con qué rol va a ingresar a Campuslands")
print("                                         ")
menu_principal = ("1. Coordinador", "2. Trainer", "3. Camper", "4. SALIR ....","5.volver")

menu_cor = ("1. registrar camper", "2. registrar notas","3. Ingresar matricula ","4. Asignar area de entrenamiento ", "5. SALIR.. ","6. Volver ")

menu_trainer = ("1. Asignar ruta","2. Asignar Horario ","3. SALIR ....","4.v Volver")

for i in menu_principal: 
    print(i)
try:
    opc = int(input("Ingrese el número del menú al que desea ingresar: "))
except ValueError:
    print("Por favor ingrese un número válido.")

if opc == len(menu_principal) -1 :
    print("                        ")
    print("SALIENDO.....")
    print("*****************************")
elif opc == 1:
    print("                         ")
    print("BIENVENIDO COORDINADOR")
    print("Escoja la opción que va a realizar")
    for u in menu_cor:
        print(u)    
    try:
        opci = int(input("Ingrese el número del menú al que desea ingresar: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        opci = 0
    if opci == len(menu_cor)-1:
        print("SALIENDO.....")
    
    elif opci == 1:
        try:
            with open(ruta_archivo, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("El archivo no existe")
            data = []
        print("****************************************************")
        datos["Doc"] = input("Ingrese su Número de Documento: ")
        datos["Nombres"] = input("Ingrese sus Nombres: ")
        datos["Apellidos"] = input("Ingrese sus Apellidos: ")
        datos["Direccion"] = input("Ingrese su Dirección de residencia: ")
        datos["Acudiente"] = input("Ingrese los Datos de su Acudiente (Nombre completo, Parentesco y Número telefónico): ")
        datos["Celular"] = input("Ingrese su Número de celular: ")
        data.append(datos)        
        with open(ruta_archivo, "w") as file:
            json.dump(data, file, indent=4)
        print("********************************************************")
        print("Se ha registrado correctamente")
        print("********************************************************")
        print(data)
    elif opci == 2:                    
        doc = input("Ingrese el documento para ingresar notas: ")
        try:
            with open(ruta_archivo, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("El archivo no existe")
            data = []
        camper = next((item for item in data if item["Doc"] == doc), None)
        if camper:
            try:
                nota_teo = int(input("Digite la nota de la prueba teórica: "))
                nota_pract = int(input("Digite la nota de la prueba práctica: "))
            except ValueError:
                print("Error de digitación, favor ingresar UNICAMENTE NÚMEROS")
                nota_teo, nota_pract = 0, 0
            prom = (nota_pract + nota_teo) / 2
            if prom >= 60:
                camper["Estado"] = "Aprobado"
                with open(ruta_archivo, "w") as file:
                    json.dump(data, file, indent=4)
                print("********************************************************")
                print("Se ha registrado correctamente")
                print("********************************************************")
                print(data)
            else:
                print("El promedio es menor a 60. No se puede aprobar.")
        else:
            print("No se encontró un camper con ese documento.")
    elif opci == 3: 
        doc = input("Ingrese el documento para nodificar ruta: ")
        try:
            with open(ruta_archivo, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("El archivo Docno existe")
            data = []
        camper = next((item for item in data if item["Doc"] == doc), None)
        if camper:
                ruta=input("ingrese el nombre de la ruta asignada(Java, NetCore, NodeJs): ")
                camper["Ruta Asignada"] = ruta
                with open(ruta_archivo, "w") as file:
                    json.dump(data, file, indent=4)
                if camper["Ruta Asignada"] =="Java" or "JAVA":
                    print("****************************************************************")
                    print("contiene los siguientes modulos: ","Fundamentos de programación","Programación Web","Programación formal","Bases de datos","Backend " )
                elif camper["Ruta Asignada"] =="NetCore" or "netcore" or "NETCORE":
                    print("****************************************************************")
                    print("contiene los siguientes modulos: ","Fundamentos de programación","Programación Web","Programación formal","Bases de datos","Backend " )  
                elif camper["Ruta Asignada"] =="NodeJs" or "nodejs" or "NODEJS":
                    print("****************************************************************")
                    print("contiene los siguientes modulos: ","Fundamentos de programación","Programación Web","Programación formal","Bases de datos","Backend " )                 
        print("********************************************************")
        print("Se ha registrado correctamente")
        print("********************************************************")
        print(data)
    elif opci == 4:
        doc = input("Ingrese el documento para asignar el aula : ")
        try:
            with open(ruta_archivo, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("El archivo no existe")
            data = []
        camper = next((item for item in data if item["Doc"] == doc), None)
        if camper:
            if camper["Ruta Asignada"] == "JAVA" or "java" or "Java":
                camper["Aula"]="Sputnik"
            with open(ruta_archivo, "w") as file:
                json.dump(data, file, indent=4)
            print("********************************************************")
            print("Se ha registrado correctamente")
            print("********************************************************")
            print (data)   
        if camper:
            if camper["Ruta Asignada"] == "NetCore" or "netcore" or "NETCORE":
                camper["Aula"]="Artemis"
            with open(ruta_archivo, "w") as file:
                json.dump(data, file, indent=4)
            print("********************************************************")
            print("Se ha registrado correctamente")
            print("********************************************************")
               
        if camper:
            if camper["Ruta Asignada"] == "NodeJs" or "nodejs" or "NODEJS":
                camper["Aula"]="Apolo"
            with open(ruta_archivo, "w") as file:
                json.dump(data, file, indent=4)
            print("********************************************************")
            print("Se ha registrado correctamente")
            print("********************************************************")
            print (data)
elif opc == 2:
    print("                            ")
    print(" BIENVENIDO TRAINER ")
    print("Escoja la opción que va a realizar")
    for t in menu_trainer:
        print(t)
    try:
        opcio = int(input("Ingrese el número del menú al que desea ingresar: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        opcio = 0
    if opcio == len(menu_trainer) -1:
        print("SALIENDO.....")
    elif opcio == 1:
        doc = input("Ingrese el documento para asignar un trainer segun la ruta a desarrollar : ")
        try:
            with open(ruta_archivo, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("El archivo no existe")
            data = []
        camper = next((item for item in data if item["Doc"] == doc), None)
        if camper:
            print=datos["Ruta Asignada"]
            trainer=input("ingrese el nombre del Trainer que va a desarrollar su ruta asignada:")
            camper["Trainer"]=trainer
        with open(ruta_archivo, "w") as file:
            json.dump(data, file, indent=4)
            print("********************************************************")
            print("Se ha registrado correctamente")
            print("********************************************************")
            print (data)
    elif opcio == 2:
        doc = input("Ingrese el documento para asignar un horario: ")
        print("Los horarios de las clases inician cada 4 horas y los horarios disponibles son","(Lunes - Virnes)","(6.00 am - 10.00 am)","(10.00am- 2.00pm)","(2.00pm-6.00pm)","(6.00p - 10.00pm)")
        try:
            opcio = int(input("Ingrese el número del menú al que desea ingresar: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            opcio = 0
            data = []
        camper = next((item for item in data if item["Doc"] == doc), None)
        if camper:
            print=datos["Ruta Asignada"]
            horario=input("ingrese el horario que mas se ajusta a usted para desarrollar la ruta programada: ")
            camper["Horario"]=horario
        with open(ruta_archivo, "w") as file:
            json.dump(data, file, indent=4)
            print("********************************************************")
            print("Se ha registrado correctamente")
            print("********************************************************")
            print (data)


