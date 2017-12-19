import pandas as pd
import numpy as np
import re
from datetime import date, timedelta, datetime

from const import *

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
        return list()
    
def get_index_with_hashtag(df, hashtag):
    """
        Returns the indices of the tweets in which the given hashtag appears.
    """
    
    return np.where(df.tag.apply(lambda x : hashtag in x))    

def search_hashtag(hashtag, df, group_hashtags):
    """Filter the given dataset to keep only elements that contain the given hashtag"""
    return df.iloc[group_hashtags.loc[hashtag].tweets_idx]

def parse_date(date_string):
    """Parse the string of format YYYY-mm-dd into a datetime.date object
    """
    return datetime.strptime(date_string, "%Y-%m-%d").date()
    
