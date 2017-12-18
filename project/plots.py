import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from datetime import date, timedelta

from const import *


def plot_frequency_tags(df, col, hashtag, n, group_tags):
    """Display a bar plot of the number of tweets with the given hashtag per day, month or year.
       The bar plot contains the 'n' days/months/years that have the most tweets about the hashtag, in chronological order."""
    dfs = search_hashtag(hashtag, df, group_tags)
    fig = plt.figure(figsize=(n/5,4))
    fig = dfs[col].value_counts()[:n].sort_index().plot.bar()
    plt.show()
    
def plot_hashtag_occurence_for_dates(hashtag, dic_tag_days, start_date, end_date):
    """Display a bar plot of the number of unique users that
       tweeted the given hashtag between the given dates.
    """
    # Get the total number of days to be displayed
    delta = end_date - start_date
    nb_days = delta.days + 1
    
    # Create the array of string containing every day between the given end and start dates
    dates = [str(start_date + timedelta(days=i)) for i in range(nb_days)]
    # Get the corresponding nuber of unique users having tweeted the hashtag
    nb_authors = [dic_tag_days.get(hashtag).get(d, 0) for d in dates]
    
    # Set the label for the xticks
    date_ticks_period = math.ceil(nb_days/50)
    date_ticks = [(dates[i] if i%date_ticks_period==0 else "") for i in range(nb_days)]
    
    # Display the bar plot
    width = 0.5 if (nb_days < 200) else 1.0
    left = [l + (1-width)/2 for l in range(nb_days)]
    plt.figure(figsize=(min(20, nb_days/4),4))
    plt.title(hashtag)
    plt.bar(left, nb_authors, width=width)
    plt.xticks(left, date_ticks, rotation='vertical')
    plt.ylabel("Number of unique users \n that tweeted the hashtag ")
    plt.show()    
    
def plot_hashtag_and_event_score(hashtag, event_score, dic_tag_days, start_date, end_date, threshold=None):
    """Display a bar plot of the number of unique users that tweeted the given hashtag
       between the given dates, and the computed event score on top.
    """
    # Get the total number of days to be displayed
    delta = end_date - start_date
    nb_days = delta.days + 1
    
    # Get the relevant portion of the event prediction
    start_day_index = (start_date - DATASET_BEGIN_DATE).days
    event_score = event_score[start_day_index : start_day_index + nb_days]
    
    # Create the array of string containing every day between the given end and start dates
    dates = [str(start_date + timedelta(days=i)) for i in range(nb_days)]
    # Get the corresponding nuber of unique users having tweeted the hashtag
    nb_authors = [dic_tag_days.get(hashtag).get(d, 0) for d in dates]
    
    # Set the label for the xticks
    date_ticks_period = math.ceil(nb_days/50)
    date_ticks = [(dates[i] if i%date_ticks_period==0 else "") for i in range(nb_days)]
    
    # Display the plot
    width = 0.5 if (nb_days < 200) else 1.0
    left = [l + (1-width)/2 for l in range(nb_days)]
    
    fig, ax1 = plt.subplots(figsize=(min(20, nb_days/4),4))
    plt.title(hashtag)
    ax2 = ax1.twinx()
    
    # Plot of number of unique authors
    ax1.bar(left, nb_authors, width=width)
    ax1.set_ylabel('Number of unique users \n that tweeted the hashtag ')
    ax1.set_xticks(left)
    ax1.set_xticklabels(date_ticks, rotation=90)
    
    # Plot of number of event score
    ax2.plot(left, event_score, 'r-')
    ax2.set_ylabel('Event prediction score')
    ax2.set_ylim(0, max(1, event_score.max()))
    for t in ax2.get_yticklabels():
        t.set_color('r')
        
    # Display a line at the event score corresponding to the threshold if it was given
    if threshold is not None:
        threshold_line = [threshold for i in range(len(event_score))]
        ax2.plot(left, threshold_line, 'k--')

    plt.show()