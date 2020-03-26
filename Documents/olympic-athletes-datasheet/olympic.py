#!/usr/local/bin/python3

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

athlete_file = "athlete_events.csv"
regions_file = "noc_regions.csv"

# read athlete csv file to variable
data = pd.read_csv(athlete_file)

# print head/describe/info of the csv file
# print the first 5 lines
# print(data.head(5))
# print count/mean/std/min/.../max of the int/float columns
# print(data.describe())
# print Column  Non-Null Count   Dtype
print(data.info())

# read regions csv file to variable
regions = pd.read_csv(regions_file)

# merge two cvs file/variable to one
merged = pd.merge(data, regions, on='NOC', how='left')
print(merged.info())

# select the Femal Gold athlete
goldMedals = merged[(merged.Medal == 'Gold') & (merged.Team == 'China')]
# goldMedals = merged[(merged.Medal == 'Gold') & (merged.Sex == 'F')]
# print(goldMedals.head(5))

# plot a bar with Year/Age
plt.figure(figsize=(12, 8))
plt.tight_layout()
# #1 counter plot
# sns.countplot(goldMedals['Age'])
# #2 scatter plot
sns.scatterplot(goldMedals['Year'], goldMedals['Age'])
# #3 bar plot
# plt.bar(goldMedals['Year'], goldMedals['Age'])
plt.title('Athlete\'s Age According to Year')
plt.xlabel('Year')
plt.ylabel('Age')
plt.show()