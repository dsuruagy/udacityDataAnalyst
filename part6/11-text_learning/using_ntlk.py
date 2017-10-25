from nltk.corpus import stopwords

sw = stopwords.words("english")
print 'quantity of stopwords on nltk:', len(sw)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("unresponsive")
print stemmer.stem("responsiveness")