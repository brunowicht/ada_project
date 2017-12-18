import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from datetime import date, timedelta

import folium
from folium.plugins import MarkerCluster

from const import *


def popup_html(row):
    """Return the html to create a popup for the dataframe row.
    """
    return """
    <style>
    h3 {
        color: black;
        font-size: 16px;
        text-align: center;
    }
    </style>
    <h3> %s </h3>
    <h3> %s </h3>
    """ %( row.day, str(row.tag.replace("'", "").replace("[", "").replace("]", "")) )

def add_markers_to_map_(dataframe, map_, popup = True, maxClusterRadius = 10):
    """Add the clusters of markers from the dataframe to the given map. 
    """
    popups = []
    coordinates = []
    for index,row in dataframe.iterrows():
        if row.Latitude != '\\N' and row.Longitude != '\\N':
            coordinates.append([float(row.Longitude), float(row.Latitude)])
            if popup:
                popups.append(folium.Popup(popup_html(row)))
            else:
                popups.append("")
            
    marker_cluster = MarkerCluster(locations=coordinates, 
                                   popups=popups).add_to(map_)
           
def get_map_with_hasthtag(hashtag, df_tag, group_hashtags, dates=None):
    """Create a map with the markers for the given hashtag and (optionally) at the given dates.
    """
    swiss_coord = [46.8, 8.2]
    swiss_map = folium.Map(swiss_coord, zoom_start=8)
    
    # Get the dataframe of the tweet containing the hashtag.
    indexes = group_hashtags.loc[hashtag]
    event_df_tag = df_tag.iloc[indexes[0]]
    
    # If some dates were given, keep only tweets from these dates
    if dates is not None:
        dates_str = [str(d) for d in dates]
        event_df_tag = event_df_tag[event_df_tag['day'].isin(dates_str)] 
    
    add_markers_to_map_(event_df_tag, swiss_map)

    return swiss_map    