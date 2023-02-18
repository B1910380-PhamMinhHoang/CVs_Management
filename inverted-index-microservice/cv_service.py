import requests

class CVService:
    @classmethod
    def get_total_cvs(cls):
        url = 'http://cv-service:5051/api/cv/total'
       
        return int(requests.get(url).json())
