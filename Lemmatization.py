from nltk.stem import WordNetLemmatizer 

def lemmatization(Word):

    lemmatizer = WordNetLemmatizer() 

    return lemmatizer.lemmatize(Word)

#print(lemmatization("disconnects"))


  


