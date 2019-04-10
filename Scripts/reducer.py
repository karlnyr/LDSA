#!/usr/bin/env python3

import sys

current_noun = None
current_count = 0
noun = None

for line in sys.stdin:
    clean_tuple = line.strip()
    noun, count = clean_tuple.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if noun == current_noun:
        current_count += count
    else:
        if current_noun:
            print('%s\t%s' % (current_noun, current_count))
        current_count = count
        current_noun = noun

if current_noun == noun:
    print('%s\t%s' % (current_noun, current_count))
