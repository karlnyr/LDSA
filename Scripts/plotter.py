import matplotlib.pyplot as plt


def plot_normalized(dictionary, count):
    """plotting the normalized tweet counts."""

    for noun in dictionary:
        dictionary[noun] = dictionary[noun] / count
    list_it = sorted(dictionary.items())
    x, y = zip(*list_it)
    plt.figure()
    plt.bar(x, y)
    plt.xlabel("Noun")
    plt.ylabel("Frequency")
    plt.title("Frequency of Swedish nouns in tweets")
    plt.savefig('noun_freq.png')


def main():
    plot_normalized(noun_freq, count)
