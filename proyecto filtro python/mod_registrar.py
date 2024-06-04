import json 
ruta_archivo = "proyecto filtro python/campers.json"
def lee_json():
    try:
        with open("proyecto filtro python/campers.json","r")as file:
            contenido = file.read()
            contenido = json.loads(contenido)
            return contenido
    except FileNotFoundError:
        print("El archivo no existe")
        print("¡¡¡ Creando Archivo  !!")
        return []    

def registrar_camper(): 
    data=lee_json()
    datos={ 
    "Doc":"",
    "Nombres":"",
    "Apellidos":"",
    "Direccion":"",
    "Acudiente":"",
    "Celular":"",
    "Estado":"proceso de ingreso ",
    "Ruta Asignada" : "",
    "Riesgo":""
    }
    datos["Doc"]=int(input("Ingrese su Número de Documento : "))
    datos["Nombres"]=(input("Ingrese sus Nombres: "))
    datos["Apellidos"]=(input("Ingrese sus Apellidos: "))
    datos["Direccion"]=(input("Ingrese su Direccion de residencia: "))
    datos["Acudiente"]=(input("Ingrese los Datos de su Acudiente (Nombre completo,Parentesco y Número telefonico):  "))
    datos["Celular"]=(int(input("Ingrese su Número de celular:  ")))
    datos["Ruta Asignada"]=(input("Ingrese la ruta que va a desarrollar el camper (NodeJs, Java, Netcore):  "))
    data.append(datos)

    with open(ruta_archivo,"w") as file:
        file.write(json.dumps(data, indent=4))
        print("********************************************************")
        print("Se ha registrado correctamente")
        print("********************************************************")
        print(data)
    return data

def nueva_ruta():
    with open(ruta_archivo, 'r') as file:
        datos = json.load('campers.json')
        datos["Ruta Asignada"]=input("seleccione la ruta que va a desarrollar (NodeJs, Java, Netcore): ")
        json.close()
