# Coronavirus Twitter Analysis

## Background

**Data**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
Only *geotagged* tweets are included in the dataset.
In total, there are about 1.1 billion tweets in this dataset, all from 2020.

The tweets are stored in a zip file for each day, which hold 24 texts files, one for each hour of the day. Within those text files, tweets are stored in JSON format.

**Objective**

Use [MapReduce](https://en.wikipedia.org/wiki/MapReduce) to anaylze the dataset and produce graphs tracking the usage of pandemic related hashtags.

## Code Overview

<code>map.py</code> processes the zip file for an indiviudal day. It tracks the usage of hashtags at the language and country level, creating a zip file for each day and level with all the tweets containing the desired hashtags.

<code>reduce.py</code> merges the outputs of <code>map.py</code> into a combined file. It produces one file for all tweets at the language and one at the country level.

<code>visualize.py</code> generates a bar chart with the country/language on the x-axis, and the number of hashtag uses on the y-axis.

For example, to generate a bar chart displaying \#cornavirus across languages in 2020, you would run the following command:
```
$ ./src/visualize.py --input_path=reduced.lang --key='#coronavirus'
```

<code>alternative_reduce.py</code> generates a line chart displaying their usage over 2020.
It can be run as follows:
```
$ ./src/alternative_reduce.py --hashtags="'#ww3', '#worldwar3', '#thirdworldwar', '#terceraguerramundial', '#guerramundial3'"
```
## Results

### Plots made with <code>visualize.py</code>

**\#coronavirus Usage by Language in 2020**

<img src=language_coronavirus.png width=50% />

**\#코로나바이러스 Usage by Language in 2020**

<img src=language_korean.png width=50% />

**\#coronavirus Usage by Country in 2020**

<img src=country_coronavirus.png width=50% />

**\#코로나바이러스 Usage by Country in 2020**

<img src=country_korean.png width=50% />

### Plot made with <code>alternative_reduce.py</code>

**Hashtag Usage Over 2020**

 <img src=line_plot.png width=50% />
