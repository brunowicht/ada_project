import pandas as pd
import numpy as np
import math
import sys
from datetime import date, timedelta

import folium

from const import *
from maps import *


def display_event_map(hashtag, dates, df_tag, group_hashtags):
    """Returns a map containing all tweets with the given hashtag at the given dates,
       and the estimated event location.
    """
    # Get the estimated event location and mean deviation
    (event_location, mean_deviation) = get_event_location(hashtag, dates, df_tag, group_hashtags)
    print("Detected event location : {}\nMean deviation : {}".format(event_location, mean_deviation))
    
    # Create the map and return it
    my_map = get_map_with_hasthtag(hashtag, df_tag, group_hashtags, dates=dates)
    folium.CircleMarker(event_location, popup='Detected event location', color='#ff0000', fill_color='#ff0000').add_to(my_map)
    return my_map

def get_tweets_with_hashtag_at_dates(hashtag, dates, df_tag, group_hashtags):
    """Get the dataframe of tweets containing the given hashtag that were tweeted at the given dates.
    """
    # convert dates to string
    dates_str = [str(d) for d in dates]
    
    # Get the tweets indices of the hashtag
    tweets_idx = group_hashtags.get_value(hashtag, 'tweets_idx')
    
    # Keeep only the tweets from the given dates
    event_df = df_tag.iloc[tweets_idx]
    event_df = event_df[event_df['day'].isin(dates_str)] 
    
    # Removes invalid locations
    event_df = event_df[event_df.Longitude != '\\N']
    event_df = event_df[event_df.Latitude != '\\N']
    
    return event_df
    
def get_event_location(hashtag, dates, df_tag, group_hashtags, event_df=None):
    """Returns the estimated event location, and the mean deviation from that location,
        as well as the mean deviation from the event location.
       The event location is obtained by the median location of all tweets 
       with the given hashtag tweeted in the given dates.
    """
    # Compute the dataframe for that event if it wasn't provided
    if event_df is None:
        event_df = get_tweets_with_hashtag_at_dates(hashtag, dates, df_tag, group_hashtags)
    
    if event_df.size == 0:
        raise ValueError('No tweets found for the given dates.')
    
    # Get the estimated event location using the median
    event_location = event_df[['Longitude', 'Latitude']].median().values
    
    # Compute the mean deviation from the event location
    df_deviation = event_df[['Longitude', 'Latitude']].applymap(lambda x: np.nan if x=='\\N' else float(x))
    df_deviation.dropna('index', how='any')
    df_deviation['Longitude'] = abs(df_deviation['Longitude'] - float(event_location[0]))
    df_deviation['Latitude'] = abs(df_deviation['Latitude'] - float(event_location[1]))
    mean_deviation = df_deviation.mean().values.max()
    
    return (event_location, mean_deviation)

def get_events_locations(event_dic, df_tag, group_hashtags, std_threshold=0.25, min_loc_nb=10, return_mean_std=False):
    """Compute the location of the detected events.
    Returns the location of each event, and the mean deviation as well if return_mean_std is True.
    It keeps only event locations for which the mean standard deviation is below std_threshold,
    and the number of tweet locations is at least min_loc_nb.
    """
    print("Computing events locations...")
    event_locations = {}
    nb_tags = len(event_dic)
    
    for tag_idx, (hashtag, dates) in enumerate(event_dic.items()):
        event_df = get_tweets_with_hashtag_at_dates(hashtag, dates, df_tag, group_hashtags)
        loc_nb = event_df.shape[0]
        
        # Compute the location only if we have a minimum of min_tweet_nb valid locations
        if loc_nb >= min_loc_nb:
            location_deviation = get_event_location(hashtag, dates, df_tag, group_hashtags, event_df=event_df)
            
            if location_deviation[1] < std_threshold:
                if return_mean_std:
                    # Save the location and mean deviation
                    event_locations[hashtag] = location_deviation
                else:
                    # Save only the location
                    event_locations[hashtag] = location_deviation[0]
        
        sys.stdout.write("\r{0:.2f}%".format((float(tag_idx+1)/nb_tags)*100))
        sys.stdout.flush()
    
    print("\n")
    return event_locations