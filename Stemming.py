import logging
from nltk.stem.snowball import SnowballStemmer

def stemming(word):
    logging.info("stemming function")
    stemmer = SnowballStemmer("english")

    return stemmer.stem(word)

#print(stemming("disconnects"))

