import logging
from nltk.stem import WordNetLemmatizer 

def lemmatization(Word):
    logging.info("lemmatization function")
    lemmatizer = WordNetLemmatizer() 

    return lemmatizer.lemmatize(Word)

#print(lemmatization("disconnects"))


  


