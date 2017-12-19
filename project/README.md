# Event detection on a Twitter dataset
[**View notebook in NbViewer**](https://nbviewer.jupyter.org/github/brunowicht/ada_project/blob/master/project/project.ipynb)

Project notebook: [project.ipynb](project.ipynb)

Project report: [ada2017.pdf](report/ada2017.pdf)

## Abstract
Social networks are widely used to discuss real-life regional and international events. In this project, we describe a way to hashtag-based event detection and localization from a dataset of tweets geolocated in Switzerland. The method proposed is effective for major incidents and popular festivities, and is suitable for events lasting one or multiple days. Our  procedure detected a total of 7082 distinct events and found 440 meaningful local events locations.

## Research questions
- How can we accurately detect events and label them based on tweets posted by Swiss users.
- How can we approximate the geographical location of a detected event.
- What trend with respect to time can be seen for the most popular events.

## Dataset
For this project, we will use the Swiss tweets dataset, which contains 22 million tweets collected between 2010-2016 and that were geolocated in Switzerland.

## Member contributions
- **Bruno:** Coming up with project main idea, data cleaning and preprocessing: filter tweets with no hashtags and store them in new CSV file, basic idea for event detection.

- **Davide:** Grouping data by hashtag, report writing, map visualisation, getting unique authors per days. Data cleaning and preprocessing.

- **Tanguy:** Event detection algorithm idea and implementation, event localisation, report writing, frequency plot and map visualisation.

**Final Presentation:**
- Bruno: Main poster idea and structure
- Davide: Poster design
- Tanguy: Speech, poster design
