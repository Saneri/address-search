#!/bin/bash

set -e

counter=0
for file in finland_address_bulks/finland_addresses_*
do
  curl -s -o /dev/null -H "Content-Type: application/x-ndjson" -X PUT "https://localhost:9200/addresses/_bulk" -ku admin:"'RQ43-3Jm&4*_D\i13sJab-2w33I9{Hb" --data-binary "@$file" 
  counter=$((counter+1))
  echo "File $counter processed."
done