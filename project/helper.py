import pandas as pd
import numpy as np
import re
import json
import matplotlib.pyplot as plt
import csv

def get_hashtags(text):
    """Returns the list of all hashtags (e.g. '#hashtag') present in the given text"""
    try:
        res = re.findall(r"#\w+", text)
        return [s.lower() for s in res]
    except:
        print(text)
        return list()
    
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


def compute_hashtag_list(df):
    """Compute the list of different hashtags and return it"""
    
    concat_list = np.concatenate(df.tag.apply(lambda x : np.array(get_hashtags(x))))
    unique_tags = np.unique(concat_list)
    return unique_tags
    
def compute_hashtag_list_and_store(df):
    """Compute the list of different hashtags and store it in a JSON file"""
    
    unique_tags = compute_hashtag_list(df)
    with open('../../twitter_dataset/unique_hashtags.json', 'w') as outfile:
        json.dump(unique_tags.tolist(), outfile)
    
def load_hashtag_list():
    """Load the list of different hashtags and return it"""
    
    with open('../../twitter_dataset/unique_hashtags.json', 'r') as infile:
        unique_tags = json.load(infile)
    return unique_tags


def search_hashtag(tag, df):
    return df[(df["tag"].str.contains(tag))]


def plot_frequency_tags(df, col, tag, n):
    dfs = search_hashtag(tag, df)
    fig = plt.figure(figsize=(n/5,4))
    fig = dfs[col].value_counts()[:n].sort_index().plot.bar()
    plt.show()