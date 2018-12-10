import requests


class WebServiceClient:

    def __init__(self, url): 
        self.session = requests.Session()
        self.url = url

    def get(self): 
        response = self.session.get(self.url)
        return response.json()

    def post(self):
        return self.session.post(self.url)
