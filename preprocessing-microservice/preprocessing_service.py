from preprocessing_util import PreprocessingUtil

class PreprocessingService:
    @classmethod
    def preprocess(
        cls, 
        text, 
        lower=True, 
        expand_contracted_words=True,
        tokenization=True, 
        lemmatization=True,
        remove_punctation=True
    ):
        result = text
        if lower == True:
            result = PreprocessingUtil.convert_into_lower(text)
        if expand_contracted_words == True:
            result = PreprocessingUtil.expand_contracted_words(result)
        if tokenization == True:
            result = PreprocessingUtil.tokenize_and_lemmatize(result, lemmatization=lemmatization)
        if remove_punctation == True:
            if tokenization == True:
                result = PreprocessingUtil.remove_punctuation_from_list(result)
            else:
                result = PreprocessingUtil.tokenize_and_lemmatize(result, lemmatization=False)
                result = PreprocessingUtil.remove_punctuation_from_list(result)
                result = " ".join(result)

        return result




