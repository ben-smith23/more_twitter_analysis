#!/usr/bin/env python3

# command line args
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#for k,v in items:
#    print(k,':',v)

items = items[:10]
keys = [item[0] for item in items]
values = [item[1] for item in items]
keys = keys[::-1]
values = values[::-1]

# create the bar graph

plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)
if 'en' in keys:
    xlabel = 'Language'
    name = 'language'
else:
    xlabel = 'Country'
    name = 'country'

if str(args.key) == '#worldwar3':
    pngkey = '_' + str(args.key)[1:]
else:
    pngkey = '_spanish'

plt.xlabel(xlabel)
plt.ylabel('Times Mentioned in Tweets')
plt.savefig(name + pngkey + '.png')
