import numpy as np
import pandas as pd
from datetime import datetime


def create_date_features(df):
    df = df.copy()

    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    df['quarter'] = df.index.quarter
    df["day_of_year"] = df.index.dayofyear
    df["week_of_year"] = df.index.isocalendar().week.astype(int)

    return df


def create_month_boundary_features(df):
    df = df.copy()

    df['is_last_day_of_month'] = df.index.is_month_end.astype(int)
    df['is_first_day_of_month'] = df.index.is_month_start.astype(int)

    return df


def create_month_position_features(df):
    """
    Create features representing the position of a date within the month.
    """

    df = df.copy()

    df["days_from_month_start"] = df.index.day - 1

    df["days_to_month_end"] = (
        df.index.to_series()
        .apply(lambda x: (x + pd.offsets.MonthEnd(0)).day - x.day)
    )

    return df

def create_all_date_features(df):

    df = create_date_features(df)
    df = create_month_boundary_features(df)

    return df
