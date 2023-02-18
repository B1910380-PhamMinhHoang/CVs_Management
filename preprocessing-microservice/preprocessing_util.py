import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, MWETokenizer
import string

nltk.download('punkt')
nltk.download('wordnet')

class PreprocessingUtil:
    expand_contracted_rules = {
        "can't": "cannot",
        "don't": "do not",
        "doesn't": "does not",
        "won't": "will not",
        "isn't": "is not",
        "aren't": "are not",
        "amn't": "am not",
        "haven't": "have not",
        "hasn't": "has not",
        "wouldn't": "would not",
        "shouldn't": "should not",
        "couldn't": "could not",
        "i'm": "i am",
        "it's": "it is",
        "he's": "he is",
        "she's": "she is",
        "you're": "you are",
        "we're": "we are",
        "they're": "they are",
        "i'll": "i will",
        "it'll": "it will",
        "he'll": "he will",
        "she'll": "she will",
        "you'll": "you will",
        "we'll": "we will",
        "they'll": "they will",
    }
    lemmatizer = WordNetLemmatizer()
    multi_words_is_a_term = [
        ("c", "#")
    ]
    tokenizer = MWETokenizer(multi_words_is_a_term)

    @classmethod
    def convert_into_lower(cls, text):
        return text.lower()

    @classmethod
    def expand_contracted_words(cls, text):
        for contracted_word in cls.expand_contracted_rules:
            if contracted_word in text:
                text = text.replace(contracted_word, cls.expand_contracted_rules[contracted_word])

        return text

    @classmethod
    def lemmatize(cls, word):
        return cls.lemmatizer.lemmatize(word, pos="v")

    @classmethod
    def tokenize_and_lemmatize(cls, text, lemmatization=True):
        words = word_tokenize(text)     
        terms = cls.tokenizer.tokenize(words)
    
        if lemmatization == True:
            terms = [cls.lemmatize(term.replace("_", " ")) for term in terms]
    
        return terms
       
    @classmethod
    def remove_punctuation_from_list(cls, words):
        new_words = []
        for word in words:
            if word not in string.punctuation:
                if word[-1] == ".":
                    word = word[:-1]
                new_words.append(word)
        
        return new_words