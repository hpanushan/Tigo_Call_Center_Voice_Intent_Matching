from nltk.stem.snowball import SnowballStemmer

def stemming(word):

    stemmer = SnowballStemmer("english")

    return stemmer.stem(word)

#print(stemming("disconnects"))

