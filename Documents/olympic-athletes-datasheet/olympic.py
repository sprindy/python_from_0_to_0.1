#!/usr/local/bin/python3

import pandas as pd
from matplotlib import pyplot as plt

athlete_file = "athlete_events.csv"
regions_file = "noc_regions.csv"

# read athlete csv file to variable
data = pd.read_csv(athlete_file)

# print head/describe/info of the csv file
#data.head(5)
print(data.head(5))
print(data.describe())
print(data.info())

# read regions csv file to variable
regions = pd.read_csv(regions_file)

# merge two cvs file/variable to one
merged = pd.merge(data, regions, on='NOC', how='left')

# select the Femal Gold athlete
goldMedals = merged[(merged.Medal == 'Gold') & (merged.Sex == 'F')]
print(goldMedals.head(5))

# plot a bar with Year/Age
plt.figure(figsize=(12, 8))
plt.bar(goldMedals['Year'], goldMedals['Age'])
plt.title('Athlete\'s Age According to Year')
plt.xlabel('Year')
plt.ylabel('Age')
plt.show()
