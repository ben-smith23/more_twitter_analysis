#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import json
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
import datetime as dt

# format args input

day_counts = {day: 0 for day in range(1, 367)}
dataset = {}

string = args.hashtags[0]
list = [s.strip("'") for s in string.split(", ")]

# count hashtag totals for each day and create dictionary dataset
for hashtag in list:
    hashtag_counts = {}
    for filename in os.listdir('./outputs/'):
        if not filename.endswith('.lang'):
            continue
        with open(os.path.join('./outputs/', filename)) as f:
            data = json.load(f)
            s = str(f)
            start = s.find('-') + 1
            end = s.find('.zip')
            day = s[start:end]
            if str(hashtag) in str(data):
                total = 0
                for lang in data[hashtag]:
                    total += data[hashtag][lang]
                    if day not in hashtag_counts:
                        hashtag_counts[day] = total
                    else:
                        hashtag_counts[day] += total
        hashtag_counts = {k: v for k, v in sorted(hashtag_counts.items())}
        dataset[hashtag] = hashtag_counts

fig, ax = plt.subplots(figsize=(12, 6))

# Set the y-axis to a logarithmic scale
ax.set_yscale('log')

# Adjust y-axis label to reflect the logarithmic scale
ax.set_ylabel('Log of Times Mentioned in Tweets')

for hashtag in dataset:
    x_values = []
    y_values = []
    for day in dataset[hashtag]:
        # Convert day string to datetime object
        try:
            date = dt.datetime.strptime(day, '%Y-%m-%d')
        except ValueError:
            continue
        x_values.append(date)
        y_values.append(dataset[hashtag][day])
    x_values.sort()
    ax.plot(x_values, y_values, label=hashtag)

# Format x-axis as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1))

ax.set_xlabel('Date')

ax.legend()

# Save plot
plt.savefig('line_plot.png')

