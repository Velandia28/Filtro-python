import json 

def lee_json():
    try:
        with open("campers.json","r")as file:
            contenido = file.read()
            contenido = json.loads(contenido)
            return contenido
    except FileNotFoundError:
        print("El archivo no existe")
        return []    


ruta_archivo = "campers.json"

def registrar_camper(): 
    data=lee_json()
    datos={ 
    "Doc":"",
    "Nombres":"",
    "Apellidos":"",
    "Direccion":"",
    "Acudiente":"",
    "Celular":"",
    "Estado":"inscrito",
    "Ruta Asignada" : "",
    "Riesgo":""
    }

    datos["Doc"]=int(input("Ingrese su Número de Documento : "))
    datos["Nombres"]=(input("Ingrese sus Nombres: "))
    datos["Apellidos"]=(input("Ingrese sus Apellidos: "))
    datos["Direccion"]=(input("Ingrese su Direccion de residencia: "))
    datos["Acudiente"]=(input("Ingrese los Datos de su Acudiente (Nombre completo,Parentesco y Número telefonico):  "))
    datos["Celular"]=(int(input("Ingrese su Número de celular:  ")))
    data.append(datos)

    with open(ruta_archivo,"w") as file:
        file.write(json.dumps(data, indent=4))
        print("Se ha registrado correctamente")
        print(data)
    return data

    
        
