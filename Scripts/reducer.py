#!/usr/bin/env python3

import matplotlib as plt
import sys


def plot_normalized(dict, count):
    """plotting the normalized tweet counts."""

    normalized_counts = [0] * len(dict.keys())
    for noun in dict:
        normalized_counts[noun] = dict[noun] / count


def main():
    noun_freq = {'han': 0, 'hon': 0, 'det': 0, 'den': 0, 'denne': 0, 'denna': 0, 'hen': 0}  # Designated words to map
    count = 0
    for noun in sys.stdin:
    clean_noun = noun.strip()
    if clean_noun.isalpha():
        if clean_noun in noun_freq:
            noun_freq[clean_noun] += 1
    elif clean_noun.isdigit():
        count += int(clean_noun)

    plt.figure()
    plt.
