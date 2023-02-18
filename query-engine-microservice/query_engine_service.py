import numpy as np
from numpy.linalg import norm
from preprocessing_service import PreprocessingService
from inverted_index_service import InvertedIndexService
from word2vec_service import Word2vecService

class QueryEngineService:
    # get from databaseeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    cv_terms = {
        "1": ["i", "love", "ariana grande", "she", "be", "a", "singer", "i", "be", "listen", "to", "her", "songs"],
        "2": ["do", "you", "like", "her", "yes", "no"],
        "3": ["my", "favorite", "program", "languages", "be", "c #", "java", "and", "javascript"],
        "4": ["my", "gpa", "be", "9.9", "my", "ip", "be", "1.2.3.4"],
        "5": ["my", "address", "be", "c #", "love", "it"]
    }

    # quản lý giá trị cosine similarity giữa query và các cv
    cv_similarities_dict = {}

    @classmethod
    def search_documents(cls, query_string):
        if query_string == '':  
            return {}   # list of all cv idddddddddddddddddddddddddddddd

        terms_of_query = PreprocessingService.preprocess(query_string)

        cls.update_cv_similarities(terms_of_query)
        print(cls.cv_similarities_dict)
        return list(sorted(cls.cv_similarities_dict.items(), key=lambda item: item[1], reverse=True))

    @classmethod
    def update_cv_similarities(cls, terms_of_query):
        for cv_id in cls.cv_terms:
            cls.cv_similarities_dict[cv_id] = cls.calc_cv_and_query_similarities(cv_id, terms_of_query)
    
    @classmethod
    def calc_cv_and_query_similarities(cls, cv_id, terms_of_query):
        if cls.jaccard(cls.cv_terms[cv_id], terms_of_query) <= 0.3:
            cv_vecto = Word2vecService.get_vecto_by_terms(cls.cv_terms[cv_id])
            query_vecto = Word2vecService.get_vecto_by_terms(terms_of_query)
        else:
            cv_vecto = InvertedIndexService.get_vecto_by_cv_id(cv_id)
            query_vecto = InvertedIndexService.get_vecto_by_query_terms(terms_of_query)

        return cls.calc_vectos_similarities(cv_vecto, query_vecto)

    @classmethod
    def jaccard(cls, a, b):
        intersection = set(a).intersection(set(b))
        union = set(a).union(set(b))

        return len(intersection) / len(union)

    @classmethod
    def calc_vectos_similarities(cls, vecto1, vecto2):
        return np.dot(vecto1, vecto2) / (norm(vecto1) * norm(vecto2))
    
   