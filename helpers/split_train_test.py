from sklearn.model_selection import train_test_split
import codecs


# with codecs.open("train.txt", "r", encoding = "utf-8") as f:
#     dataset = f.read()

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

#sentences = get_sentences(dataset)
#train, test = train_test_split(sentences, test_size=0.2)
with codecs.open("datasets/train.txt", "r", encoding = "utf-8") as f:
    semi_train_text = f.read()
train = get_sentences(semi_train_text)

# with codecs.open("test.txt", "r", encoding = "utf-8") as f:
#     test_text = f.read()
# test = get_sentences(test_text)

def build_dataset(dataset):
    data = ['']
    for words in dataset:
        data.append('\n'.join(words))
        data.append('')
    return '\n'.join(data)

# with codecs.open("test.txt", "w", encoding = "utf-8") as f:
#     f.write(build_dataset(test))

# with codecs.open("semi_train.txt", "w", encoding = "utf-8") as f:
#     f.write(build_dataset(train))


def split_quote_and_spark(dataset):
    quote, spark = [], []
    for index in range(len(dataset)):
        if dataset[index][0][0].lower() == "s":
            spark.append(dataset[index])
        else:
            quote.append(dataset[index])
    return quote, spark

q_train, s_train = split_quote_and_spark(train)
#q_test, s_test = split_quote_and_spark(test)

def save(path, dataset):
    with codecs.open(path, "w", encoding = "utf-8") as f:
        f.write(build_dataset(dataset))

save("datasets/q_train.txt",q_train)
save("datasets/s_train.txt", s_train)

# save("q_test.txt", q_test)
# save("s_test.txt", s_test)

