def predict(model, X):
    return model.predict(X)


def predict_probability(model, X):
    return model.predict_proba(X)