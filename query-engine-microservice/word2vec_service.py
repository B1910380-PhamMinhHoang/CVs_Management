import gensim.downloader as api
import numpy as np

class Word2vecService:
    w2v = api.load('word2vec-google-news-300')
        
    @classmethod
    def convert_word_into_vecto_by_word2doc(cls, word):
        return cls.w2v[word] if word in cls.w2v else np.zeros(300)

    @classmethod
    def get_vecto_by_terms(cls, terms):
        return np.mean([cls.convert_word_into_vecto_by_word2doc(term) for term in terms], axis=0)

