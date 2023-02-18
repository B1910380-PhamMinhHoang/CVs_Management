from flask import Flask, request
from query_engine_service import QueryEngineService

app = Flask(__name__)

@app.route('/api/query_engine/search', methods=['POST'])
def search_cvs():
    query_string = request.json['query_string'] if ('query_string' in request.json) else ''

    return QueryEngineService.search_documents(query_string)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)