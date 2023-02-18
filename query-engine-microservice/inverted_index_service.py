import requests

class InvertedIndexService:
    @classmethod
    def get_vecto_by_cv_id(cls, cv_id):
        url = 'http://inverted-index-service:5004/api/inverted_index/vecto_of_cv/' + cv_id
        
        return requests.get(url).json()
    
    @classmethod
    def get_vecto_by_query_terms(cls, terms):
        url = 'http://inverted-index-service:5004/api/inverted_index/vecto_of_query'
        body = { 'query': terms }
        
        return requests.post(url, json = body).json()
