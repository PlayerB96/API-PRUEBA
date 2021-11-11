import json
import logging
import time
import requests
from logging.handlers import RotatingFileHandler



from homologacion import Api

class Retransmision:
    
    @staticmethod
    def apiHomologacion(token):
        api = Api()
        token = api.resultsHomologacion(token)
        return token

    def ejecution(self):

        token = "d92ffc2de10ae0c2b4608dc4c9086d8614529C61371DF6B38111B4549D90F303F85C30F4"
        registro = self.apiHomologacion(token)

        # for row in registro['items']:

        #     logging.basicConfig(filename='./homologacion.log', format='%(message)s', level=logging.ERROR)
           
        #     logging.error(row['nm'])
        # logging.error('Se envio Trama Nombre     -    ')
        # lista=[]   
        for row in registro['items']:
            if row['pos'] == None:
                objTemp = {
                        'latitud':'',
                        'longitud':'',
                        'velocidad': 0,
                        'placa':'',
                        'posicion':'apagado'
                        
                }
            elif row['pos']['s'] > 0 :    
                objTemp = {
                        'latitud':str(row['pos']['x']),
                        'longitud':str(row['pos']['y']),
                        'velocidad': str(row['pos']['s']),
                        'placa':str(row['nm']),
                        'posicion':'en ruta'
                        
                }
            
            else :    
                objTemp = {
                        'latitud':str(row['pos']['x']),
                        'longitud':str(row['pos']['y']),
                        'velocidad': str(row['pos']['s']),
                        'placa':str(row['nm']),
                        'posicion':'detenido'
                        
                }
            
            # lista.append(objTemp)
            # print(objTemp)
            if row['pos'] != None:
                objToken = 'https://geocode-maps.wialon.com/hst-api.wialon.com/gis_geocode?coords=[{"lon":'+objTemp['latitud']+',"lat":'+objTemp['longitud']+'}]&flags=1255211008&uid=21734836'
                result = requests.get(objToken)
                # print(result)
                json_result = json.loads(result.text)
                
        
            else :
                json_result[0] = ' No hay Direccion......'
            print(json_result[0])
            # dir = json.dumps(json_result)
            # print(json_result)
            # print(str(dir))
            vel = int(objTemp['velocidad'])
            # print(objTemp['posicion'])
            pos = objTemp['posicion']
            if pos == 'en ruta' :
                objFinal = {
                            'placa':str(row['nm']),
                            'posicion' : "en ruta",
                            'velocidad' : vel,
                            'direccion' : str(json_result)
                }
            elif pos == 'detenido'  :
                 objFinal = {
                            'placa':str(row['nm']),
                            'posicion' : "detenido",
                            'velocidad' : vel,
                            'direccion' : str(json_result)
                }
            else :
                 objFinal = {
                            'placa':str(row['nm']),
                            'posicion' : "apagado",
                            'velocidad' : vel,
                            'direccion' : str(json_result)
                }
            # dir = json.dumps(json_result)
            # print(json_result)
            # obj = json.dumps(objFinal['direccion'])
            # nobj = str(obj)[3:-3]
            # print(json_result)

            logging.basicConfig(filename='./homoDireccion.log', format='%(message)s', level=logging.ERROR)
            # print(row['pos']) 
            logging.error(objFinal['placa'] +', '+ objFinal['posicion'] +', '+ json_result[0])
            # logging.error(' LATITUD          -     LONGITUD   ')  



# while True:
print(str(Retransmision().ejecution()))
    # time.sleep(3)
    
    