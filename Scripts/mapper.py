#!/usr/bin/env python3
import json
import sys
import re

"""The purpose of this script is to  """

count = 0  # Number of total unique tweets read from process.
nouns = ['han', 'hon', 'det', 'den', 'denne', 'denna', 'hen']  # Designated words to map


for line in sys.stdin:
    if not line == '\n':
        json_line = json.loads(line)
        try:  # Using error when searching dictionary missing Key
            json_line['retweeted_status']
        except KeyError:
            for word in json_line['text'].lower().split():
                if word in nouns:
                    print(f"{word}")  # Printing out touples to std.in
            count += 1
print(f"{count}")
