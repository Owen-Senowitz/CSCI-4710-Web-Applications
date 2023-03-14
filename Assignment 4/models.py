import pandas as pd

def read_classmate_data():
    return pd.read_csv('classmate_data.csv')

def write_classmate_data(df):
    df.to_csv('classmate_data.csv', index=False)
