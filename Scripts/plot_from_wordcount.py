import fileinput
import matplotlib.pyplot as plt


class characters:
    """Characters extracted from input"""

    def __init__(self, word, count):
        self.word = word
        self.count = int(count)


def main():
    array_characters = []
    for line in fileinput.input():
        split_lines = line.split("\t")
        array_characters.append(characters(split_lines[0], split_lines[1].rstrip('\n')))
    X = [None] * len(array_characters)
    Y = [None] * len(array_characters)
    for word in range(len(array_characters)):
        X[word] = array_characters[word].word
        Y[word] = array_characters[word].count
    fig = plt.figure('word_counts')
    plt.plot(X, Y)
    plt.xlabel("Character starting word")
    plt.ylabel("Counts")
    fig.savefig('word_counts.png')


main()
