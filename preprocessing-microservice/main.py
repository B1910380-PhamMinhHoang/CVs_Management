from flask import Flask, request
from preprocessing_service import PreprocessingService

app = Flask(__name__)

@app.route('/api/preprocessing/text', methods=['POST'])
def preprocessing():
    # return tokens and skillssssssssssssssssssss
    lower_param = request.args.get('lower')
    if (lower_param == None) or (lower_param == 'true'):
        lower_param = True
    
    expand_contracted_words_param = request.args.get('expand_contracted_words_param')
    if (expand_contracted_words_param == None) or (expand_contracted_words_param.lower() == 'true'):
        expand_contracted_words_param = True
    
    tokenization_param = request.args.get('tokenization')
    if (tokenization_param == None) or (tokenization_param == 'true'):
        tokenization_param = True

    lemmatization_param = request.args.get('lemmatization')
    if (lemmatization_param == None) or (lemmatization_param == 'true'):
        lemmatization_param = True

    remove_punctation_param = request.args.get('remove_punctation')
    if (remove_punctation_param == None) or (remove_punctation_param == 'true'):
        remove_punctation_param = True

    return PreprocessingService.preprocess(
        text=request.json['text'],
        lower=(lower_param == True),
        expand_contracted_words=(expand_contracted_words_param == True),
        tokenization=(tokenization_param == True), 
        lemmatization=(lemmatization_param == True),
        remove_punctation=(remove_punctation_param == True)
    )

if __name__ == '__main__':
    app.run(port = 5000, debug = True)