import pandas as pd
import numpy as np
import re
import json
import matplotlib.pyplot as plt

def get_hashtags(text, lowercase=True):
    """Returns the list of all hashtags (e.g. '#hashtag') present in the given text
    
    text: text from which the hashtags should be extracted
    lowercase: if True, convert hashtags all teh extracted hashtags to lowercase
               if False, return the hashtags as they were in the given text
    """
    try:
        res = re.findall(r"#\w+", text)
        if lowercase:
            return [s.lower() for s in res]
        else:
            return res
    except:
        print(text)
        return list()
    
def get_index_with_hashtag(df, hashtag):
    """
        Returns the indices of the tweets in which the given hashtag appears.
    """
    
    return np.where(df.tag.apply(lambda x : hashtag in x))    

def get_mentions(t):
    """Returns the list of all mentions (e.g. '@mention') present in the given text"""
    return re.findall(r"@\w+", t)

def add_lines_in_df(lines, dataframe):
    df2 =  pd.DataFrame(lines)
    df2.columns = col
    df2 = df2[keep_col]
    df2['tag'] = df2.text.apply(lambda t: get_hashtags(t))
    df2['at'] = df2.text.apply(lambda t: get_mentions(t))
    df2 = df2[keep_final]
    return pd.concat([dataframe, df2], ignore_index=True)


def search_hashtag(hashtag, df):
    """Filter the given dataset to keep only elements that contain the given hashtag"""
    return df[(df["tag"].str.contains(hashtag))]

def plot_frequency_tags(df, col, hashtag, n):
    """Display a bar plot of the number of tweets with the given hashtag per day, month or year.
       The bar plot contains the 'n' days/months/years that have the most tweets about the hashtag, in chronological order."""
    dfs = search_hashtag(hashtag, df)
    fig = plt.figure(figsize=(n/5,4))
    fig = dfs[col].value_counts()[:n].sort_index().plot.bar()
    plt.show()
