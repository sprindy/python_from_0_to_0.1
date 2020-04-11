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
# print(regions.info())
# print(regions.head(3))
# merge two cvs file/variable to one
merged = pd.merge(data, regions, on='NOC', how='left')
# print(merged.info())
# print(merged.head(3))


# select the Femal Gold athlete
# goldMedals = merged[(merged.Medal == 'Gold')]
goldMedals = merged[(merged.Medal == 'Gold') & (merged.Team == 'China')]
# goldMedals = merged[(merged.Medal == 'Gold') & (merged.Sex == 'M')]
# goldMedals = merged['Medal'] == 'Gold'][merged['Sex'] == 'F']
# print(goldMedals.head(5))
# print(goldMedals.info())


# plot a bar with Year/Age
plt.figure(figsize=(12, 8))
plt.tight_layout()
plt.title('Athlete\'s Age According to Year')
plt.xlabel('Year')
plt.ylabel('Age')
# rotate xlable for 30 degree
plt.xticks(rotation=30)

# 选择哪种plot绘图
plot_index = 11
if (1 == plot_index):
    # #1 bar plot
    plt.bar(goldMedals['Year'], goldMedals['Age'])
elif (2 == plot_index):
    # #2 scatter plot
    plt.scatter(goldMedals['Year'], goldMedals['Age'])
elif (3 == plot_index):
    # #3 pie plot
    teamPie = goldMedals['Team'][goldMedals['Year'] == 2004]
    print(teamPie)
    # plt.pie(x=teamPie., labels=teamPie)
elif (11 == plot_index):
    # #11 counter plot
    sns.countplot(goldMedals['Age'])
elif (12 == plot_index):
    # #12 scatter plot
    sns.scatterplot(goldMedals['Year'], goldMedals['Age'])
elif (13 == plot_index):
    olderThan45 = goldMedals['Sport'][goldMedals['Age'] > 45]
    # [goldMedals['Sex'] == 'F']
    # print(olderThan45)
    sns.countplot(olderThan45)

if (0 != plot_index):
    plt.show()