import pandas as pd
from sklearn.metrics import confusion_matrix

# Check a dataframe for nulls,
# print/report them in a nice "pretty" format


def null_df(df):
    new_df = df.isnull()
    return print(new_df)


# Report a confusion matrix,
# with labels for easier interpretation


def confusion_labels(y_pred, y_true):
    names = []
    matrix = confusion_matrix(y_true, y_pred, labels=names)
    return matrix


# Single function to take a list, turn it into a series
# and add it to a dataframe as a new column

def list_to_series(df):
    new = pd.Series(list)
    new = df.append(new, axis=1)
    return new


# Split addresses into multiple columns city, state zip

def split_address(df):
    new_df = pd.DataFrame({df['city'], df['state'], df['zip']})
    return new_df
