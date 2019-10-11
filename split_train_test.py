from sklearn.model_selection import train_test_split
import codecs


with codecs.open("train.txt", "r", encoding = "utf-8") as f:
    dataset = f.read()

def get_sentences(dataset):
    dataset = dataset.split("\n")
    sentences, words = [], []
    for word in dataset[1:]:
        if len(word) == 0:
            sentences.append(words)
            words = []
        else:
            words.append(word)
    return sentences

sentences = get_sentences(dataset)
train, test = train_test_split(sentences, test_size=0.2)

def build_dataset(dataset):
    data = ['']
    for words in dataset:
        data.append('\n'.join(words))
        data.append('')
    return '\n'.join(data)

with codecs.open("test.txt", "w", encoding = "utf-8") as f:
    f.write(build_dataset(test))

with codecs.open("semi_train.txt", "w", encoding = "utf-8") as f:
    f.write(build_dataset(train))