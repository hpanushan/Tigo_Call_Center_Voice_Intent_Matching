from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

def stemming(Word):

    ps = PorterStemmer() 

    return ps.stem(Word)

