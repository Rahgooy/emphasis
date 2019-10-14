import matplotlib.pyplot as plt
from collections import defaultdict
from nltk.stem import PorterStemmer as stemmer

def pos_counter(pos_lsts, pos_dict):
    for pos in pos_lsts:
        if pos[0] in pos_dict:
            pos_dict[pos[0]] += 1
        elif pos in pos_dict:
            pos_dict[pos] += 1
        else:
            pos_dict["Other"] += 1
    return pos_dict


def pie_fig(items, explode = ()):
    labels = items.keys()
    sizes = items.values()
    _, ax1 = plt.subplots(figsize = (5,5))
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal') 
    plt.show()

def get_bold_occurrences_word(word_vocab, word_probs):
    """return word occurences with  maximum probabilty in each senteces """
    bold_occurrences_word = defaultdict(int)
    for i in range(len(word_vocab)):
        max_indx , max_value = -1, 0
        for j in range(len(word_vocab[i])):
            word_prob = float(word_probs[i][j])
            if max_value < word_prob:
                max_value, max_indx = word_prob , j
        bold_occurrences_word[stemmer().stem(word_vocab[i][max_indx].lower())] += 1
    return bold_occurrences_word

def get_occurrences_word(word_vocab):
    words_vocab = [stemmer().stem(word.lower()) for innerlist in word_vocab for word in innerlist]
    occurrences_word = defaultdict(int)
    for word in words_vocab:
        occurrences_word[word] += 1
    return occurrences_word


def calculate_freqs_probs(bold_occurrences_item, occurrences, occurrences_threshold = 20, probs_threshold = 10):
    probs, freqs , items = [],[],[]
    for item ,bold_freq in bold_occurrences_item.items():
        if occurrences[item] > occurrences_threshold and (bold_freq/occurrences[item])*100 > probs_threshold:
            probs.append( (bold_freq/occurrences[item])* 100)
            freqs.append(occurrences[item])
            items.append(item)
    return probs, freqs, items

def scatter_plot(x, y, labels, x_label, y_label, xlim = True):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    for i, word in enumerate(labels):
        ax.annotate(word, (x[i], y[i]))
    if xlim:
        plt.xlim(0, 400)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def get_bio_freqs_word(bio_freqs, word_lsts):
    bio_freqs_word = defaultdict(int)
    for i in range(len(bio_freqs)):
        for j in range(len(bio_freqs[i])):
            bio = bio_freqs[i][j].split("|")
            word_stem = stemmer().stem(word_lsts[i][j].lower())
            bio_freqs_word[word_stem] += (int(bio[0]) + int(bio[1]))
    return bio_freqs_word


def calculate_bio_probs(bio_freqs_word, occurrences_word, bio_range = [50, 1000], occurrences_range= [50, 400]):
    bios_probs, words_freq, words = [], [], []
    for key, value in bio_freqs_word.items():
        if value < bio_range[1] and value > bio_range[0]:
            if occurrences_word[key] > occurrences_range[0] and occurrences_word[key] < occurrences_range[1]:
                bios_probs.append((value/(occurrences_word[key]*9))*100)
                words_freq.append(occurrences_word[key])
                words.append(key)
    return bios_probs, words_freq, words


def get_bio_freqs_pos(bio_freqs, pos_lsts):
    bio_freqs_pos = defaultdict(int)
    occurrences_pos = defaultdict(int)
    for i in range(len(bio_freqs)):
        for j in range(len(bio_freqs[i])):
            bio = bio_freqs[i][j].split("|")
            bio_freqs_pos[pos_lsts[i][j]] += (int(bio[0]) + int(bio[1]))
            occurrences_pos[pos_lsts[i][j]] += 1
    return bio_freqs_pos, occurrences_pos