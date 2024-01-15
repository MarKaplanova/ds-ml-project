import pandas as pd

def drop_columns(dataframe, columns):
    dataframe = dataframe.drop(columns, axis=1)
    return dataframe

def interpolate_by(dataframe, columns):
    dataframe = dataframe.groupby(columns).apply(lambda group: group.interpolate(method='linear', limit_direction = 'both')).reset_index(drop = 1)
    return dataframe

def sort_by(dataframe, columns):
    dataframe.sort_values(columns)
    return dataframe