import nltk
from nltk.corpus import stopwords 
from Lemmatization import lemmatization
from Stemming import stemming

def intent_matching(text):
    # convert text into lowercase
    text = text.lower()

    # Keywords
    # Monthly,daily,charged?
    recharge_issue = ['balanc','topup','credit','recharg','reload']
    service_failure = ['activ','deactiv','data','voice','packag','servic','packag','subscrib','unsubscrib','subscript',
                        'unsubscript','basi','bill','alert']                       
    network_faiulre = ['speed','slow','2g','3g','4g','network','signal','strength','coverag','poor','nois','disconnect','area']

    ## Convert text to set of words
    nltk_tokens = nltk.word_tokenize(text)
    unique_tokens = set(nltk_tokens)

    # Stropwords removal
    stop_words = set(stopwords.words('english')) 

    filtered_tokens = [w for w in unique_tokens if not w in stop_words] 
    print(filtered_tokens)

    ## Converting each tokens to root format
    # Stemming - (originated-->origin , learning-->learn)
    # Lemmatization - (skills-->skill) (Handles same meaning tokens)
    
    root_tokens = []
    print("")
    for token in filtered_tokens:
        stemmed = stemming(token)
        lemmatized = lemmatization(token)

        if (stemmed==lemmatized):
            root_tokens.append(stemmed)

        else:
            root_tokens.append(stemmed)

    return root_tokens


text = """


hello I am calling to know if my recharge balance
 thank you but also is there another way that I can check all these balances rather than always calling is there anything I should know that I can check balances
 okay thank you


"""

print(intent_matching(text))