import requests

class PreprocessingService:
    @classmethod
    def preprocess(cls, text):
        url = 'http://preprocessing-service:5003/api/preprocessing/text'
        body = { 'text': text }
        
        return requests.post(url, json = body).json()
