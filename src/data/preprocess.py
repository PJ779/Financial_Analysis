from src.features.transformations import apply_log_transformation, apply_yeo_johnson, scale_features
from src.config import LOG_COLUMNS, YEO_COLUMNS

def preprocess_data(X_train, X_test):

    if LOG_COLUMNS:
        X_train = apply_log_transformation(X_train, LOG_COLUMNS)
        X_test = apply_log_transformation(X_test, LOG_COLUMNS)

    if YEO_COLUMNS:
        X_train, X_test, pt = apply_yeo_johnson(
            X_train,
            X_test,
            YEO_COLUMNS,
        )

    X_train, X_test, scaler = scale_features(
        X_train,
        X_test,
    )

    return X_train, X_test, pt, scaler

