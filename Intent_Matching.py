import nltk
from nltk.corpus import stopwords 
from Lemmatization import lemmatization
from Stemming import stemming

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

def intent_matching(text):
    print("Running intent matching feature......")
    # convert text into lowercase
    text = text.lower()

    # Counts
    counts = {
        'network_issue' : 0,
        'recharge_issue' : 0,
        'service_issue' : 0
    }

    # Keywords
    db_obj = MySQL_Intents_Keywords('146.148.85.146','root','Omnibis.1234','speech')
    network_issue = db_obj.read_column_data('network_issue')
    recharge_issue = db_obj.read_column_data('recharge_issue')
    service_issue = db_obj.read_column_data('service_issue')

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
        if token in network_issue:
            counts['network_issue'] += 1

        elif token in recharge_issue:
            counts['recharge_issue'] += 1
        
        elif token in service_issue:
            counts['service_issue'] += 1

        else: pass

    print("Counting number of keywords for each intent")
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
