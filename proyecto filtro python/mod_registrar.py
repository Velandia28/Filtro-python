import json

datos={ 
"Doc":[],
"Nombre":[],
"Apellidos":[],
"Direccion":[],
"Acudiente":[],
"Celular":[],
"Estado":"inscrito",
"Ruta Asignada" : "",
"Riesgo":""
}

ruta_archivo = "campers.json"

def registrar_camper(data):
    contenido = json.dumps(datos,indent=4)
    if data.get[Doc,]=="":
        camper={}
        Doc=int(input("Ingrese su Número de Documento : "))
        Nombre=(input("Ingrese sus Nombres: "))
        Apellido=(input("Ingrese sus Apellidos: "))
        Direccion=(input("Ingrese su Direccion de residencia: "))
        Acudiente=(input("Ingrese los Datos de su Acudiente (Nombre completo,Parentesco y Número telefonico):  "))
        Celular=(int(input("Ingrese su Número de celular:  ")))
        Estado=(input("Su estado Actual en Campus es : "))
    
    
    try:
        with open (camper,"w")as file:
            file.write(contenido)
            print("Datos guardados con exito!!")
    except Exception:
        print("Error al guardar datos ")
    datos.data["datos"]
    camper.json.data.append(datos)[Doc],Nombre,Apellido,Direccion,Acudiente,Celular,Estado