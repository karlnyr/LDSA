#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys


def plot_normalized(dictionary, count):
    """plotting the normalized tweet counts."""

    for noun in dictionary:
        dictionary[noun] = dictionary[noun] / count
    list_it = sorted(dictionary.items())
    x, y = zip(*list_it)
    plt.figure()
    plt.bar(x, y)
    plt.xlabel(f"Noun")
    plt.ylabel(f"Frequency")
    plt.savefig('noun_freq.png')


def main():
    """Designating the main lattice used for noun selection)"""

    noun_freq = {'han': 0, 'hon': 0, 'det': 0, 'den': 0, 'denne': 0, 'denna': 0, 'hen': 0}  # Designated words to map
    count = 0
    for noun in sys.stdin:
        clean_noun = noun.strip()
        if clean_noun.isalpha():
            if clean_noun in noun_freq:
                noun_freq[clean_noun] += 1
        elif clean_noun.isdigit():
            count += int(clean_noun)
    plot_normalized(noun_freq, count)


main()
