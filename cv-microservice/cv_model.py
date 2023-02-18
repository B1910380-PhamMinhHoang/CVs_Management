class CV:
    def __init__(self, _id, file_path, terms, folder_id, extra_data):
        self._id = _id
        self.file_path = file_path
        self.terms = terms
        self.folder_id = folder_id
        self.extra_data = extra_data

    def to_dict(self):
        return {
            'id': self._id,
            'file_path': self.file_path,
            'terms': self.terms,
            'folder_id': self.folder_id,
            'extra_data': self.extra_data
        }