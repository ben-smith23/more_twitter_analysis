#!/bin/bash

for input_file in /data/Twitter\ dataset/geoTwitter20-*.zip; do
  echo "Running map.py on $input_file"
 
  nohup ./src/map.py --input_path="${input_file}" &
done

