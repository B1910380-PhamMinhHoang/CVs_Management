from cv_model import CV
from tika import parser
import re
import requests
from preprocessing_service import PreprocessingService
from inverted_index_service import InvertedIndexService
import os

class CVService:
    cvs = []
    id_counter = len(cvs) + 1
    
    @classmethod
    def get_all_cvs(cls):
        return cls.cvs

    @classmethod
    def find_cvs_by_folder_id(cls, folder_id):
        return list(filter(lambda cv: cv.folder_id == folder_id, cls.cvs))

    @classmethod
    def get_total_cvs(cls):
        return str(len(cls.cvs))
        
    @classmethod
    def create_cv(cls, cv_file, extra_data_dict):
        if (cv_file is None) or (cv_file.filename == ''):
            return None

        cv_id = str(cls.id_counter)
        file_path = cls.get_cv_file_path(str(cv_id))
        cv_file.save(file_path)

        folder_id = '#'
        if ('folder_id' in extra_data_dict):
            folder_id = extra_data_dict['folder_id'][0]
            del extra_data_dict['folder_id']
        text_in_cv = cls.convert_pdf_into_text(file_path)
        terms = PreprocessingService.preprocess(text_in_cv)
        InvertedIndexService.insert_terms_of_cvs(cv_id, terms)

        cv = CV(cv_id, file_path, terms, folder_id, extra_data_dict)
        cls.id_counter += 1
        
        cls.cvs.append(cv)

        return cv

    @classmethod
    def get_cv_file_path(cls, cv_id):
        return 'cvs/cv_' + cv_id + '.pdf'

    @classmethod
    def convert_pdf_into_text(cls, file_path):
        raw_text = parser.from_file(file_path)

        return re.sub("\n+|\uf0b7|\s{2,}", "", raw_text['content'])

    @classmethod
    def delete_cv(cls, cv_id):
        new_cvs = []
        deleted_cv = None
        for cv in cls.cvs:
            if cv._id == cv_id:
                deleted_cv = cv
                InvertedIndexService.delete_cv_info_by_id(cv_id)
                if os.path.exists('cvs/cv_' + cv_id + '.pdf'):
                    os.remove('cvs/cv_' + cv_id + '.pdf')
            else:
                new_cvs.append(cv)
        cls.cvs = new_cvs
        
        return deleted_cv