from flask import Flask, request
from folder_model import Folder
from folder_service import FolderService

app = Flask(__name__)

@app.route('/api/folder', methods=['GET'])
def get_all_folders():
    folders = FolderService.get_all_folders()
    folder_dicts = list(map(lambda folder: folder.to_dict(), folders))

    return folder_dicts

@app.route('/api/folder', methods=['POST'])
def create_folder():
    folder = Folder.from_json(request.json)
    new_folder = FolderService.create_folder(folder)

    return new_folder.to_dict()

if __name__ == '__main__':
    app.run(port = 5000, debug = True)