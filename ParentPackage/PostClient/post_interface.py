import requests
import json

class PostInterface:
    
    def __init__(self):
        self.payload = {}
        self.url = ''

    def setPayload(self,url,payload):
        self.payload=payload
        self.url=url

    def postPayload(self):
        r = requests.post(self.url,json=self.payload)
        # print('posting-> ' ,self.payload)
        return r

