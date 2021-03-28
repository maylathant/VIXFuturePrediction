from sklearn.ensemble import RandomForestRegressor

class VIXPredict:

    def __init__(self):
        pass

    def fitModel(self, X, y, **kwargs):
        self.model = RandomForestRegressor(**kwargs)
        self.model.fit(X,y)

    def predict(self, x):
        return self.model.predict(x)
