from flask import Flask, request
from cv_model import CV
from cv_service import CVService
from werkzeug.datastructures import ImmutableMultiDict
import json

app = Flask(__name__)

@app.route('/api/cv', methods=['GET'])
def get_all_cvs():
    cvs = CVService.get_all_cvs()
    cv_dicts = list(map(lambda cv: cv.to_dict(), cvs))

    return cv_dicts

@app.route('/api/cv/folder/unknown', methods=['GET'])
def find_cvs_of_unknown_folder():
    cvs = CVService.find_cvs_by_folder_id('#')
    cv_dicts = list(map(lambda cv: cv.to_dict(), cvs))

    return cv_dicts

@app.route('/api/cv/folder/<folder_id>', methods=['GET'])
def find_cvs_by_folder_id(folder_id):
    cvs = CVService.find_cvs_by_folder_id(folder_id)
    cv_dicts = list(map(lambda cv: cv.to_dict(), cvs))

    return cv_dicts

@app.route('/api/cv/total', methods=['GET'])
def get_total_cvs():
    return CVService.get_total_cvs()

@app.route('/api/cv', methods=['POST'])
def create_cv():
    file = None if ('cv' not in request.files) else request.files['cv']
    extra_data = request.form
    if isinstance(request.form, ImmutableMultiDict):
        extra_data = request.form.to_dict(flat=False) 
    cv = CVService.create_cv(file, extra_data)
    
    return {} if (cv is None) else cv.to_dict()

@app.route('/api/cv/<cv_id>', methods=['DELETE'])
def delete_cv(cv_id):
    cv = CVService.delete_cv(cv_id)
    
    return {} if (cv is None) else cv.to_dict()

if __name__ == '__main__':
    app.run(port = 5000, debug = True)