import pandas as pd

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

def train_xgboost(X_train, y_train, **kwargs,):
    model = XGBClassifier(**kwargs,)
    model.fit(X_train, y_train)

    return model

def train_lightgbm(X_train, y_train, **kwargs):
    model = LGBMClassifier(**kwargs)
    model.fit(X_train, y_train)

    return model
    

def train_catboost(X_train, y_train, **kwargs):
    model = CatBoostClassifier(**kwargs)
    model.fit(X_train, y_train)

    return model

def train_random_forest(X_train, y_train, **kwargs):
    model = RandomForestClassifier(**kwargs)
    model.fit(X_train, y_train)

    return model

def train_adaboost(X_train, y_train, **kwargs):
    model = AdaBoostClassifier(**kwargs)
    model.fit(X_train, y_train)

    return model