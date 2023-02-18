from flask import Flask, request
from inverted_index_service import InvertedIndexService

app = Flask(__name__)

@app.route('/api/inverted_index', methods=['GET'])
def get_inverted_index():
    return InvertedIndexService.get_inverted_index()

@app.route('/api/inverted_index/insert_terms', methods=['POST'])
def insert_terms_of_cvs():
    # request.json: {
    #     cv_id: [terms],
    #     cv_id: [terms],
    # }
    return InvertedIndexService.insert_terms_of_cvs(request.json)

@app.route('/api/inverted_index/delete_cv_info/<cv_id>', methods=['DELETE'])
def delete_cv_info_by_id(cv_id):
    return InvertedIndexService.delete_cv_info_by_id(cv_id)

@app.route('/api/inverted_index/vecto_of_cv/<cv_id>', methods=['GET'])
def get_vecto_by_cv_id(cv_id):
    return InvertedIndexService.get_vecto_by_cv_id(cv_id)

@app.route('/api/inverted_index/vecto_of_query', methods=['POST'])
def get_vecto_by_query_terms():
    # request.json: {
    #     query: [terms]
    # }
    terms = [] if ('query' not in request.json) else request.json['query']
    
    return InvertedIndexService.get_vecto_by_query_terms(terms)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)