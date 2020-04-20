import nltk
from nltk.corpus import stopwords 
from Lemmatization import lemmatization
from Stemming import stemming

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

def intent_matching(text):
    # convert text into lowercase
    text = text.lower()

    # Counts
    counts = {
        'recharge_issue' : 0,
        'service_failure' : 0,
        'network_faiulre' : 0
    }

    # Keywords
    # Monthly,daily,charged,account?
    recharge_issue = ['balanc','topup','credit','recharg','reload','exceed','money','amount','card','payment','bank']
    service_failure = ['activ','deactiv','data','voice','packag','servic','packag','subscrib','unsubscrib','subscript',
                        'unsubscript','basi','bill','alert','regist','unregist','overcharg','expir']                       
    network_faiulre = ['speed','slow','2g','3g','4g','network','signal','strength','coverag','poor','nois','disconnect',
                        'area','internet','load','connect','slowdown']

    ## Convert text to set of words
    nltk_tokens = nltk.word_tokenize(text)
    unique_tokens = set(nltk_tokens)

    # Stropwords removal
    stop_words = set(stopwords.words('english')) 

    filtered_tokens = [w for w in unique_tokens if not w in stop_words] 

    ## Converting each tokens to root format
    # Stemming - (originated-->origin , learning-->learn)
    # Lemmatization - (skills-->skill) (Handles same meaning tokens)
    
    root_tokens = []
   
    for token in filtered_tokens:
        stemmed = stemming(token)
        lemmatized = lemmatization(token)

        if (stemmed==lemmatized):
            root_tokens.append(stemmed)

        else:
            root_tokens.append(stemmed)
    print(root_tokens)
    # Counting keywords for each intent
    for token in root_tokens:
        if token in recharge_issue:
            counts['recharge_issue'] += 1
        
        elif token in service_failure:
            counts['service_failure'] += 1

        elif token in network_faiulre:
            counts['network_faiulre'] += 1

        else: pass


    # Sorting dictionary by its value
    counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
    
    # Selecting the case with maximum value
    max_count =  max(counts.values())   

    if max_count==0:
        return ['Another issue']

    else:
        # Calculating the threshold
        threshold = max_count * 0.55        
    
        # Checking the cases with max value
        issues = [k for k,v in counts.items() if v >= threshold]

        return issues
