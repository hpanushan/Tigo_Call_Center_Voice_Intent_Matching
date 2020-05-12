import logging
import nltk
from nltk.corpus import stopwords 
from Lemmatization import lemmatization
from Stemming import stemming

from MySQL_DB.MySQL_Intents_Keywords import MySQL_Intents_Keywords
from Create_Issue_Count import create_issue_count
from Get_Keywords import get_keywords

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

def intent_matching(text):
    logging.info("intent matching function")
    # convert text into lowercase
    text = text.lower()

    # Counts (dictionary)
    counts = create_issue_count()

    # Keywords (dictionary)
    keywords = get_keywords()

    ## Convert text to set of words
    logging.info("tokenization")
    nltk_tokens = nltk.word_tokenize(text)
    logging.info("filtering unique tokens")
    unique_tokens = set(nltk_tokens)

    # Stropwords removal
    stop_words = set(stopwords.words('english')) 

    logging.info("removing stopwords tokens")
    filtered_tokens = [w for w in unique_tokens if not w in stop_words] 

    ## Converting each tokens to root format
    # Stemming - (originated-->origin , learning-->learn)
    # Lemmatization - (skills-->skill) (Handles same meaning tokens)
    
    root_tokens = []
    logging.info("retrieving unique tokens")
    for token in filtered_tokens:
        stemmed = stemming(token)
        lemmatized = lemmatization(token)

        if (stemmed==lemmatized):
            root_tokens.append(stemmed)

        else:
            root_tokens.append(stemmed)
    
    # Counting keywords for each intent
    logging.info("counting keywords for each intent")
    for token in root_tokens:
        for i in keywords:
            if token in keywords[i]:
                counts[i] = counts[i] + 1

    # Sorting dictionary by its value
    logging.info("sorting intents according to keyword counts")
    counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
    
    # Selecting the case with maximum value
    max_count =  max(counts.values())   

    if max_count==0:
        logging.info("maximum keyword count is zero")
        return ['Another issue']

    else:
        logging.info("returning issues for given threshold")
        # Calculating the threshold
        threshold = max_count * 0.55        
    
        # Checking the cases with max value
        issues = [k for k,v in counts.items() if v >= threshold]

        return issues
