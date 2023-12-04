import requests
from datetime import datetime, timezone

class ProccessNetbox():

    def __init__(self):
        url = "http://137.184.18.229:8000/api/dcim/devices/"

        payload = {}
        files=[

        ]
        headers = {
          'Authorization': 'token 4560d44e6a2c66a8a703947d204eed2d671c6da4'
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        self._devices = response.json()

    def validate_new_device(self, fecha):
        formate = "%Y-$m-%dT%H:%M:%S.%fZ"
        print(fecha)




    def proccess_device(self):
        result=[]

        for devices in self._devices.get('results', []):
            if devices.get('device_role', {}).get('name')=='jcp':
                self.validate_new_device(devices.get('created'))
                info_device ={
                  'id': devices.get('id'),
                  'name': devices.get('name'),
                  'custom_fields': devices.get('custom_fields', {}).get('ntp_config',{}),
                  'created': devices.get('created'),
                  'last_updated': devices.get('last_updated'),
                  'new_device': False
                }

                result.append(info_device)
        
        print(result)

    

inst = ProccessNetbox()
inst.proccess_device()





"""class NetboxChecking(object):
    def netbox(self):
        return{'get_device_config'}"""