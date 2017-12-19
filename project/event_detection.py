import pandas as pd
from datetime import date, timedelta, datetime
import numpy as np
import math
import sys

from const import *
from helper import *


def get_average(hashtag, dic_tag_days, start_date, end_date):
    """Returns the average number of unique authors of the given hashtag between the given dates.
    """
    # Get the total number of days to be displayed
    delta = end_date - start_date
    nb_days = delta.days + 1
    
    # Create the array of string containing every day between the given end and start dates
    dates = [str(start_date + timedelta(days=i)) for i in range(nb_days)]
    # Get the corresponding number of unique users having tweeted the hashtag
    nb_authors = [dic_tag_days.get(hashtag).get(d, 0) for d in dates]
    
    mean = np.mean(nb_authors)
    return mean

def group_days_list(days_list, max_days_diff):
    """Groups the given list of dates.
    max_days_diff : maximum number of days of difference for two dates to be grouped together
    """
    if len(days_list) <= 1:
        grouped_days_list = days_list
    else:
        prev_day = None
        day_group = []
        grouped_days_list = []
        
        # Iterate over the list of dates
        for i in range(0, len(days_list)):
            cur_day = parse_date(days_list[i])
            if len(day_group)==0:
                day_group.append(days_list[i])
            else:
                day_diff = (cur_day - prev_day).days
                if day_diff <= max_days_diff:
                    # Add date to current group
                    day_group.append(days_list[i])
                else:
                    # Add current group to list of groups
                    grouped_days_list.append(day_group)
                    day_group = [days_list[i]]
                    
            prev_day = cur_day
        
        if len(day_group)!=0:
            grouped_days_list.append(day_group)
            
    return grouped_days_list

def group_events_by_date(event_dic, max_days_diff=2):
    """Groups the events detected for each hashtag by date.
    max_days_diff : maximum number of days of difference for two dates to be grouped together
    """
    grouped_event_dic = {}
    for hashtag, days in event_dic.items():
        grouped_event_dic[hashtag] = group_days_list(days, max_days_diff)
        
    return grouped_event_dic