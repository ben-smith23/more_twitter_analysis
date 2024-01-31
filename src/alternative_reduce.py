#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags',nargs = '+',  required=True)
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

#print(type(args), args.hashtags[0])

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

# create line plot
fig, ax = plt.subplots()
for hashtag in dataset:
	x_values = []
	y_values = []
	days = 0
	for day in dataset[hashtag]:
		days += 1
		# convert day string to datetime object
		try:
			date = dt.datetime.strptime(day, '%m-%d')
		except ValueError:
			continue
		x_values.append(date)
		y_values.append(dataset[hashtag][day])
	x_values.sort()
	ax.plot(x_values, y_values, label=hashtag)

# format x-axis as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
y_format = mtick.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x/100000))
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1, bymonth=range(0, 13, 3)))
ax.yaxis.set_major_formatter(y_format)
ax.set_xlabel('Date')
ax.set_ylabel('Times Mentioned in Tweets (tens of thousands)')
ax.legend()

# save plot
plt.savefig('line_plot.png')
