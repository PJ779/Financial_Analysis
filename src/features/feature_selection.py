import numpy as np
import pandas as pd

def get_high_correlation_features(
    df: pd.DataFrame,
    threshold: float = 0.90,
):
    corr_matrix = df.corr().abs()

    upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )

    cols_to_drop = [
        column
        for column in upper.columns
        if any(upper[column] > threshold)
    ]


    return cols_to_drop