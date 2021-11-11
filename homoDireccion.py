import requests
import json

class Api:
    
    def __init__(self):
        #-- Token
        self.token = 'http://hst-api.wialon.com/wialon/ajax.html?svc=token/login&params='
        #-- 
        self.get = '''http://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params=
                {
                    "spec":
                    {
                        "itemsType":"avl_unit",
                        "propName":"sys_name",
                        "propValueMask":"*",
                        "sortType":"sys_name",
                        "propType":"propitemname"
                    },
                    "force":1,  
                    
                    "flags":9217,
                    "from":0,
                    "to":0}&sid='''
        
    def tokenhomoDireccion(self,token):
        objToken = '{"token":"' + str(token) +'","fl": "2"}'
        result = requests.get(str(self.token) + str(objToken))
        # print(self.token)
        json_result=json.loads(result.text)
        # print(json_result)
        eid=json_result["eid"]
        # print(eid)
        return eid

    def resultshomoDireccion(self, token):
        sid = self.tokenHomologacion(token)
        result = requests.get(self.get + str(sid))
        # print(sid)
        json_result=json.loads(result.text)
        # print(json_result)
        return json_result
    
    