#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--output_folder', default='~/bigdata/more_twitter_analysis/outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load keywords
hashtags = [
    '#ww3',  # English
    '#worldwar3',  # English
    '#thirdworldwar',  # English
    '#globalconflict',  # English
    '#waralert',  # English
    '#militaryconflict',  # English
    '#internationaltension',  # English
    '#nuclearthreat',  # English
    '#geopoliticalcrisis',  # English
    '#globalcrisis',  # English
    '#militarycrisis',  # English
    '#warpreparation',  # English
    '#conflictzone',  # English
    '#warnews',  # English
    '#warupdate',  # English
    '#الحربالعالميةالثالثة',  # Arabic for "World War 3"
    '#terceraguerramundial',  # Spanish for "Third World War"
    '#troisièmeguerremondiale',  # French for "Third World War"
    '#dritterweltkrieg',  # German for "Third World War"
    '#terzaguerramondiale',  # Italian for "Third World War"
    '#第三次世界大戦',  # Japanese for "Third World War"
    '#세계대전3',  # Korean for "World War 3"
    '#третьямироваявойна',  # Russian for "Third World War"
    '#dünyaSavaşı3',  # Turkish for "World War 3"
    '#guerramundial3',  # Portuguese for "World War 3"
    '#världskriget3',  # Swedish for "World War 3"
    '#wereldoorlog3',  # Dutch for "World War 3"
    '#maailmansota3',  # Finnish for "World War 3"
    '#verdenskrig3',  # Norwegian for "World War 3"
    '#światowawojna3',  # Polish for "World War 3"
    '#विश्वयुद्ध3',  # Hindi for "World War 3"
    '#โลกสงคราม3',  # Thai for "World War 3"
    '#जागतिकयुद्ध3',  # Marathi for "World War 3"
    '#உலகப்போர்3',  # Tamil for "World War 3"
    '#ప్రపంచయుద్ధం3',  # Telugu for "World War 3"
    '#ಜಾಗತಿಕಯುದ್ಧ3',  # Kannada for "World War 3"
    '#ലോകയുദ്ധം3',  # Malayalam for "World War 3"
    '#עולמיתמלחמה3',  # Hebrew for "World War 3"
    '#دنیاکیجنگ3',  # Urdu for "World War 3"
    '#dunyākījaṅg3',  # Romanized Urdu for "World War 3"
    '#guerramundial3',  # Catalan for "World War 3"
    '#wereldoorlog3',  # Afrikaans for "World War 3"
    '#pasaulinkarš3',  # Lithuanian for "World War 3"
    '#pasauliniskarstrekas3',  # Latvian for "World War 3"
    '#maailmansõda3',  # Estonian for "World War 3"
    '#svjetskirat3',  # Croatian for "World War 3"
    '#светскарат3',  # Serbian for "World War 3"
    '#световнавойна3',  # Bulgarian for "World War 3"
    '#világHáború3',  # Hungarian for "World War 3"
    '#guerramondiale3',  # Romanian for "World War 3"
    '#pasaulioKaras3',  # Lithuanian for "World War 3"
    '#světováválka3',  # Czech for "World War 3"
    '#svetovávojna3',  # Slovak for "World War 3"
    '#svjetskirat3',  # Bosnian for "World War 3"
    '#дунияуруш3',  # Uzbek for "World War 3"
    '#дүйнөлүксогуш3',  # Kyrgyz for "World War 3"
    '#dünyaSavaşı3',  # Azerbaijani for "World War 3"
    '#дунёуруши3',  # Tajik for "World War 3"
    '#дүниежүзіліксоғыс3',  # Kazakh for "World War 3"
    '#dunyajüziliksoğıs3',  # Romanized Kazakh for "World War 3"
    '#мироваявойна3',  # Belarusian for "World War 3"
]


# initialize counters
counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every file within the zip file
    for i,filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(),args.input_path,filename)

        # open the inner file
        with archive.open(filename) as f:

            # loop over each line in the inner file
            for line in f:

                # load the tweet as a python dictionary
                tweet = json.loads(line)

                # convert text to lower case
                text = tweet['text'].lower()

                # search hashtags
                for hashtag in hashtags:
                    lang = tweet['lang']
                    country = tweet['place']['country_code'] if tweet['place'] else None
                    if hashtag in text:
                        counter_lang[hashtag][lang] += 1
                        if country:
                            counter_country[hashtag][country] += 1
                    counter_lang['_all'][lang] += 1
                    if country:
                        counter_country['_all'][country] += 1


# open the outputfile
try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))

output_path_lang = output_path_base+'.lang'
print('saving',output_path_lang)
with open(output_path_lang,'w') as f:
    f.write(json.dumps(counter_lang))

output_path_country = output_path_base+'.country'
print('saving',output_path_country)
with open(output_path_country,'w') as f:
    f.write(json.dumps(counter_country))
