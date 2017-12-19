import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from datetime import date, timedelta

import folium
from folium.plugins import MarkerCluster

from const import *


def popup_html(text_line_1, text_line_2):
    """Return the html to create 2-lines popup to be used in maps.
    """
    return """
    <style>
    h3 {
        color: black;
        font-size: 14px;
        text-align: center;
    }
    </style>
    <h3> %s </h3>
    <h3> %s </h3>
    """ %( text_line_1, text_line_2 )

def popup_df_row(row):
    """Return the html to create a popup for the dataframe row.
    """
    return popup_html(row.day, str(row.tag.replace("'", "").replace("[", "").replace("]", "")))

def add_markers_to_map_(dataframe, map_, popup = True, maxClusterRadius = 10):
    """Add the clusters of markers from the dataframe to the given map. 
    """
    popups = []
    coordinates = []
    for index,row in dataframe.iterrows():
        if row.Latitude != '\\N' and row.Longitude != '\\N':
            coordinates.append([float(row.Longitude), float(row.Latitude)])
            if popup:
                popups.append(folium.Popup(popup_df_row(row)))
            else:
                popups.append("")
            
    marker_cluster = MarkerCluster(locations=coordinates, 
                                   popups=popups).add_to(map_)
           
def get_map_with_hasthtag(hashtag, df_tag, group_hashtags, dates=None):
    """Create a map with the markers for the given hashtag and (optionally) at the given dates.
    """
    swiss_coord = [46.8, 8.2]
    swiss_map = folium.Map(SWISS_COORD, zoom_start=8)
    
    # Get the dataframe of the tweet containing the hashtag.
    indexes = group_hashtags.loc[hashtag]
    event_df_tag = df_tag.iloc[indexes[0]]
    
    # If some dates were given, keep only tweets from these dates
    if dates is not None:
        dates_str = [str(d) for d in dates]
        event_df_tag = event_df_tag[event_df_tag['day'].isin(dates_str)] 
    
    add_markers_to_map_(event_df_tag, swiss_map)

    return swiss_map

def get_events_map(grouped_events_locations, event_dic):
    swiss_map = folium.Map(SWISS_COORD, zoom_start=8)
    
    coordinates = []
    popups = []
    for hashtag, value in grouped_events_locations.items():
        for dates, location in value:
            coordinates.append(location)
            popups.append(folium.Popup("{} \n {}".format(hashtag, ', '.join([str(d) for d in dates])), parse_html=True))
        
    MarkerCluster(locations=coordinates, popups=popups).add_to(swiss_map)
    
    return swiss_map