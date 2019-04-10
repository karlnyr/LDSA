#!/usr/bin/env python3

import sys


def main():
    """Designating the main lattice used for noun selection)"""

    noun_freq = {'han': 0, 'hon': 0, 'det': 0, 'den': 0, 'denne': 0, 'denna': 0, 'hen': 0}  # Designated words to map
    counter = 0
    for noun in sys.stdin:
        clean_tuple = noun.strip()
        noun, count = clean_tuple.split('\t', 1)
        try:
            count = int(count)
        except ValueError:
            continue
        if noun in noun_freq:  # Catch the words
            noun_freq[noun] += 1
        elif noun == 'count':  # Catch the count
            counter = int(count)

    for noun in noun_freq:
        noun_freq[noun] = noun_freq[noun] / count

    print(noun_freq)


main()
