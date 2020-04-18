import nltk
from nltk.corpus import stopwords 
from Lemmatization import lemmatization
from Stemming import stemming

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

    # Calculating the threshold
    threshold = max_count * 0.5        
    
    # Checking the cases with max value
    issues = [k for k,v in counts.items() if v >= threshold]

    return issues



text = """


hello hello so my network has been having some issues but I subscribe for a service also few months a few weeks back actually a month ago and but I expected it to work but then after the first few days it doesn't work I don't get any notifications regards to that can you please look into this yeah my my number is 07762 411 that is correct yes can you please check on it online
 yeah the network issue is very common in this area but yeah just I need this subscription sorted for now because God that is the most easiest thing that affects at this time because you know network is much more Hardware rather than software so I'm okay thank you thank you




"""

print(intent_matching(text))