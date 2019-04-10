import fileinput
import matplotlib.pyplot as plt


def plot_normalized():
    """plotting the normalized tweet counts."""

    array_characters = []
    x = []
    y = []
    normaliser = 0
    for line in fileinput.input():
        word, count = line.rstrip('\n').split("\t")
        if word == 'count':
            normaliser = int(count)
        else:
            x.append(word)
            y.append(int(count))
    for i in range(len(y)):
        y[i] = y[i] / normaliser
    # y = y / normaliser
    fig = plt.figure('word_counts')
    plt.bar(x, y)
    plt.xlabel("Character starting word")
    plt.ylabel("Counts")
    plt.title("Counts of characters starting a word")
    fig.savefig('noun_frequency.png')


plot_normalized()
