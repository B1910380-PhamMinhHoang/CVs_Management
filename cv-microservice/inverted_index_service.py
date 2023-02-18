import requests

class InvertedIndexService:
    @classmethod
    def insert_terms_of_cvs(cls, cv_id, terms):
        url = 'http://inverted-index-service:5004/api/inverted_index/insert_terms'
        body = { cv_id: terms }
        
        return requests.post(url, json = body).json()

    @classmethod
    def delete_cv_info_by_id(cls, cv_id):
        url = 'http://inverted-index-service:5004/api/inverted_index/delete_cv_info/' + cv_id
        
        return requests.delete(url).json()
