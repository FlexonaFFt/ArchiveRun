from sklearn.base import RegressorMixin

class MeanRegressor(RegressorMixin):
    def fit(self, X=None, y=None):
        self.mean = y.mean()
        return self

    def predict(self, X=None):
        return [self.mean] * len(X)

from collections import Counter
from sklearn.base import ClassifierMixin

class MostFrequentClassifier(ClassifierMixin):
    def fit(self, X=None, y=None):
        # Используем Counter для нахождения наиболее частого значения
        self.most_frequent = Counter(y).most_common(1)[0][0]
        return self

    def predict(self, X=None):
        return [self.most_frequent] * len(X)
