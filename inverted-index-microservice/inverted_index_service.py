import math
from cv_service import CVService

class InvertedIndexService:
    # inverted_index = {
    #     term: { cv_id: term_frequency, ... },
    #     ...
    # }
    inverted_index = {}

    # idf_dict = {
    #     term: term_idf,
    #     ...
    # }
    idf_dict = {}

    # all cvs and thier total terms
    total_terms_of_cvs = {}

    total_cvs = 0   # total cvs in databaseeeeeeeeeee
    
    cv_vectos_dict = {}

    @classmethod
    def get_inverted_index(cls):
        return cls.inverted_index

    @classmethod
    def insert_terms_of_cvs(cls, terms_dict):
        cls.total_cvs = CVService.get_total_cvs()
        for cv_id in terms_dict:              
            terms_inserted = terms_dict[cv_id]
            new_terms = cls.insert_terms_of_cv_to_inverted_index_and_get_new_terms(cv_id, terms_inserted)
            cls.update_idf_dict_of_terms(terms_inserted)
            cls.total_terms_of_cvs[cv_id] = len(terms_inserted)    # update total_terms_of_cvs with a new cv
            cls.update_old_cv_vectos(terms_inserted, new_terms)
            cls.cv_vectos_dict[cv_id] = cls.convert_terms_of_cv_to_vecto(cv_id)
        
        return { 'message': 'Success' }

    @classmethod
    def insert_terms_of_cv_to_inverted_index_and_get_new_terms(cls, cv_id, terms):
        new_terms = []
        for term in terms:
            if term in cls.inverted_index:
                if cv_id in cls.inverted_index[term]:
                    cls.inverted_index[term][cv_id] += 1
                else:
                    cls.inverted_index[term][cv_id] = 1
            else:
                new_terms.append(term)
                cls.inverted_index[term] = { cv_id: 1 }
        
        return new_terms

    @classmethod
    def update_idf_dict_of_terms(cls, terms_updated):
        for term in cls.inverted_index:
            if term in terms_updated:
                total_cvs_contain_term = len(cls.inverted_index[term].keys())
                cls.idf_dict[term] = math.log((cls.total_cvs + 1) / (total_cvs_contain_term + 1))

    @classmethod
    def update_old_cv_vectos(cls, terms_inserted, new_terms):
        term_list = list(cls.inverted_index.keys())
        term_inserted_indexes = [term_list.index(term) for term in terms_inserted]
        new_terms_indexes = [term_list.index(term) for term in new_terms]
        old_terms_indexes = list(filter(lambda index: index not in new_terms_indexes, term_inserted_indexes))
        
        for cv_id in cls.cv_vectos_dict:
            for i in range(len(new_terms_indexes)):
                cls.cv_vectos_dict[cv_id].append(0)
            
            for term_index in old_terms_indexes:
                tf_tdf_of_term_after_inserted = cls.calc_tf_idf_of_term_in_cv(term_list[term_index], cv_id)
                cls.cv_vectos_dict[cv_id][term_index] = tf_tdf_of_term_after_inserted

    @classmethod
    def convert_terms_of_cv_to_vecto(cls, cv_id):
        vecto = []
        for term in cls.inverted_index:
            vecto.append(
                cls.calc_tf_idf_of_term_in_cv(term, cv_id)
            )
            
        return vecto

    @classmethod
    def calc_tf_idf_of_term_in_cv(cls, term, cv_id):
        tf = 0
        if cv_id in cls.inverted_index[term]:
            term_frequency_in_cv = cls.inverted_index[term][cv_id]
            tf = term_frequency_in_cv / cls.total_terms_of_cvs[cv_id]
        
        return tf * cls.idf_dict[term]

    @classmethod
    def delete_cv_info_by_id(cls, cv_id):
        for term in cls.inverted_index:
            if cv_id in cls.inverted_index[term]:
                del cls.inverted_index[term][cv_id]
        if cv_id in cls.cv_vectos_dict:
            del cls.cv_vectos_dict[cv_id]

        return cv_id

    @classmethod
    def get_vecto_by_cv_id(cls, cv_id):
        if cv_id not in cls.cv_vectos_dict:
            vecto = [0] * len(cls.inverted_index.keys())
        else:
            vecto = cls.cv_vectos_dict[cv_id]

        return vecto
    
    @classmethod
    def get_vecto_by_query_terms(cls, terms):
        query_inverted_index_dict = cls.create_query_inverted_index_dict_by_terms(terms)
        query_verto = []
        for term in cls.inverted_index:
            tf = 0
            if term in query_inverted_index_dict:
                term_frequency_in_query = query_inverted_index_dict[term]
                total_terms_in_doc = len(query_inverted_index_dict.keys())
                tf = term_frequency_in_query / total_terms_in_doc
            query_verto.append(tf * cls.idf_dict[term])

        return query_verto

    @classmethod
    def create_query_inverted_index_dict_by_terms(cls, terms):
        query_inverted_index_dict = {}
        for term in terms:
            if term in query_inverted_index_dict:
                query_inverted_index_dict[term] += 1
            else:
                query_inverted_index_dict[term] = 1

        return query_inverted_index_dict