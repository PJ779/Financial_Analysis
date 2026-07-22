import numpy as np
import pandas as pd
from sklearn.preprocessing import PowerTransformer, StandardScaler


def apply_log_transformation(df, columns
) -> pd.DataFrame:
    df = df.copy()

    for col in columns:
        if col in df.columns:
            df[col] = np.log(df[col])

    return df

def apply_yeo_johnson(X_train,
    X_test, columns):

    """
    Apply a Yeo-Johnson power transformation.

    Fits the transformer on the training data and
    applies the learned transformation to both the
    training and test sets.

    Returns
    -------
    X_train 
    X_test 
    transformer : PowerTransformer
    """
    pt = PowerTransformer(method='yeo-johnson')
    X_train = X_train.copy()
    X_test = X_test.copy()


    X_train[columns] = pt.fit_transform(X_train[columns])
    X_test[columns] = pt.transform(X_test[columns])


    return X_train, X_test, pt


def scale_features(X_train: pd.DataFrame,
    X_test: pd.DataFrame,):
    temporal_features = [feature for feature in X_train.columns if 'Year' in feature or 'Yr' in feature]
    discrete_features = [feature for feature in X_train.columns if X_train[feature].nunique() < 31 and
                         feature not in temporal_features and 
                         pd.api.types.is_numeric_dtype(X_train[feature])]
    ignored_features = set(temporal_features + discrete_features)
    continuous_features = [
        feature for feature in X_train.columns 
        if feature not in ignored_features 
        and pd.api.types.is_numeric_dtype(X_train[feature])
    ]
    
    if not continuous_features:
        return X_train, X_test, None
    
    scaler = StandardScaler()
        
        # Create copies to avoid SettingWithCopy warnings
    X_train = X_train.copy()
    X_test = X_test.copy()
        
        # Fit on train, transform both
    X_train[continuous_features] = scaler.fit_transform(X_train[continuous_features])
    X_test[continuous_features] = scaler.transform(X_test[continuous_features])
        
    return X_train, X_test, scaler
