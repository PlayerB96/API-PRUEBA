import json
import requests

r = requests.get("https://rickandmortyapi.com/api/character/?page=2", params = {"id":28})
if r.status_code == 200:
    data = json.loads (r.text)
    # print(data["info"]["count"])
    # print(len(data["results"]))
    
    personajes=[]
    for item in data["results"]:
        # print(item["name"])
    # print(data["results"][0]["name"])
        objtemp = {
        "nombre": item["name"],
        "genero": item["gender"],
        "nombreorigen": item["origin"]["name"]
        }
        # print(objtemp)
        personajes.append(objtemp)
        
    # print(personajes)
    
    
    integrantes = [
        {
            "nombre": "Bryan",
            "edad": "25"        
        },
        {
            "nombre": "Abraham",
            "edad": "22"        
        },
        {
            "nombre": "Gerson",
            "edad": "24"        
        }
    ]
    
    nintegrantes=[]
    for item in integrantes:
  
        r = requests.get("https://api.agify.io/?name="+item["nombre"])

        # print(r.text)
        if r.status_code == 200:
            dato = json.loads (r.text)
           
        # print(dato)
        errorp = (((dato["age"])-int((item["edad"])))/int((item["edad"])))*100
        errorporc = int(abs(errorp))
        errortext = str(errorporc) + "%"
        # print(errortext)
        # print(dato["age"])
        # print(item["edad"]) 
        objtem = {
        "edad predecida": dato['age'],
        "error" : errortext,
        "nombre" : item["nombre"],
        "edad" : item["edad"]
        }
        
        nintegrantes.append(objtem)
        
    print(nintegrantes)
    
    with open('integrante.txt', 'w') as temp_file:
        for item in nintegrantes:
            temp_file.write("%s\n" % item)
    file = open('integrante.txt', 'r')
    # print(file.read())
    
    

    
