import nltk.stem
from sklearn.feature_extraction.text import CountVectorizer

english_stemmer = nltk.stem.SnowballStemmer('english')

class StemmedCountVectorizer(CountVectorizer):
    """
    Class used to build the stemmed count vectorizer english analyzer
    -----
    Methods
    -----
    build_analyzer(self)
        builds the english analyzer
    """
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()

        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
        