# Reaction of the Swiss Twitter community to major events
Our current pipeline can be found in the notebook [cleaning.ipynb](cleaning.ipynb).

## Abstract
Social networks now have a huge importance in our lives and many people use them to comment about events that are happening around the globe. With this project, we would like to see how the Swiss Twitter community reacts to important events happening in Switzerland or around the world. Our main goal is to determine to what extent and how well we can learn about what is happening in the world or in our country based on the Swiss tweets. The story we want to tell is the evolution of tweets during important events between 2010 and 2016 and discover what kind of events Swiss people are tweeting about the most. We are motivated to do this project and tell this story because none of us are active on Twitter and we're interested in understanding better how twitter is used in Switzerland.

## Research questions
- How can we accurately detect events and label them based on tweets posted by Swiss users.
- How can we approximate the geographical location of a detected event.
- What trend with respect to time can be seen for the most popular events.

## Dataset
For this project, we will use the Swiss tweets dataset, which contains 22 million tweets collected between 2010 and 2016 that were geolocated in Switzerland. We could try to see if there are periods when the activity on twitter is higher than usually and if so, link them to actual events. We could also do this by looking at the most recurrent hashtags in a certain period of time (for instance #Rio2016, #JeSuisCharlie, #fukushima, ...). Additionally, we could use geolocation to detect more local events.

## A list of internal milestones up until project milestone 3
### 1. Get familiar with the dataset 
1. Learn how to access the dataset, easily process it and deal with its size
2. Understand what specific field the dataset contains, and how it is structured
3. Determine which fields are useful and which aren't
4. Detect potential problems with the dataset (missing values, formatting inconsistencies, ...)

### 2. Cleaning and pre-processing
1. Extract a list of all the hashtags in the dataset
2. For every hashtag, get the list of tweets in which it appears
3. Aggregate the data obtained by date

### 3. Data analysis and visualization
1. Create visualizations to understand of how the popularity of a hashtag can change over time
2. Create visualizations to understand how geographical location is linked with certain hashtags
3. For some known hashtag linked to an event, vizualize its geographical repartition and popularity over time.

### 4. Event detection
1. Find a way to differentiate hashtags linked to events from ever-popular ones.
2. Create a basic algorithm for event detection using hashtag popularity and test its performance
3. Optimize the algorithm based on the results (e.g. give less importance to events with high frequency, use the userId to discriminate against events that were only tweeted by a few people, use geolocation to fine tune the algorithm, ...)
4. Find a way to approximate the geolocation of an event based on the tweets about that event
