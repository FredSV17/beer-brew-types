import pandas as pd


#Função para remover os limitadores default do jupyter notebook
def remove_limiters():
    print("Setting limiters to none")
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000
    pd.set_option('display.max_colwidth', None)  # or 199


def one_hot(database, column):
    onehot = pd.get_dummies(database[column])
    concat_data = pd.concat([database,onehot], axis=1)
    concat_data = concat_data.drop(column,axis=1)
    return concat_data

def group_data(database, column):
    database.groupby(column).mean()
    return database

