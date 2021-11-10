import json
import logging
import time
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
        # nregistro=[]
        # with open('homologacion14.txt', 'w') as temp_file:

        # LOG_FILENAME = '/homologacion2.log'
        # logger360 = logging.getLogger('homologacion')
        # logger360.setLevel(logging.DEBUG)
        # handler = logging.handlers.RotatingFileHandler(
        #   LOG_FILENAME, maxBytes=20, backupCount=5)
        # logger360.addHandler(logging.FileHandler('./homologacion2.log'))
        # handler.setLevel(logging.CRITICAL)
        # logger360.addHandler(handler)

        # # nregistro = []
        # log_formatter = logging.Formatter()

        # logFile = './homologacion3.log'

        # my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
        #                                 backupCount=2, encoding=None, delay=0)
        # my_handler.setFormatter(log_formatter)
        # my_handler.setLevel(logging.INFO)

        # logger360 = logging.getLogger('root')
        # logger360.setLevel(logging.INFO)

        # logger360.addHandler(my_handler)
        for row in registro['items']:

            # nregistro.append(row['nm'])
            # temp_file.write("%s\n" % row["nm"])  
            logging.basicConfig(filename='./homologacion.log', format='%(message)s', level=logging.ERROR)
           
            logging.error(row['nm'])
        logging.error('Se envio Trama Nombre     -    ')     
            # logger360.error(row["nm"])
                # print(row)    
        # file = open('homologacion8.txt', 'r')
                # registro.token(row)
                # y = json.dumps(nregistro)
            
            # print(*nregistro, sep = ',')
            # print(type(nregistro))
            
        # with open('homologacion11.txt', 'w') as temp_file:
        #     for item in nregistro:
        #         var = item
        #         temp_file.write("%s\n" % var )  
        #         print(var)
        # file = open('homologacion8.txt', 'r')
        

while True:
    print(str(Retransmision().ejecution()))
    time.sleep(3)
    
    