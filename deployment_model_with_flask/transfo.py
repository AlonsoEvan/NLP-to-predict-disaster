import process 
import process2

from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.pipeline import FeatureUnion


class clean(BaseEstimator, TransformerMixin):
    def __init__(self):
        return 
    
    def fit(self, mots, y = None):
        return self
    
    def transform(self, mots, y = None):
        for i in range(len(mots)):
            mots[i] = process.clean_text(mots[i])
            mots[i] = process2.clean(mots[i])
        return mots