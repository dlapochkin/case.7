"""Case-study_7
Разработчики:
Кривошапова Д.Е. 40%
Лапочкин Д.А. 30%
Кузнецов А.Д. 45%
"""
import re, random, string


def start() :
    """
    Makes text simple to be ready by the program
    :return: 'raw' text

    """
    with open(input('Введите имя файла: ')) as f_in:
        file_text = ''
        for line in f_in:
            r = line.strip()
            file_text += r + ' '
        return file_text


def associations(raw, uniq):
    """
    Creates list of words associations
    :param raw: all words from the text
    :param uniq: list of uniq words
    :return: list of words associations
    """
    words = []
    for word in uniq:
        raw_copy = raw.copy()
        that = []
        for i in range(raw.count(word)):
            ind = raw_copy.index(word)
            raw_copy.remove(word)
            if ind != len(raw_copy) and raw_copy[ind] not in that:
                that.append(raw_copy[ind])
        words.append(that)
    return words


def unic(a):
    """
    creates list of uniq words
    :param a: all words
    :return: list of uniq words
    """
    unic_list = []
    words = a.split()
    for i in words:
        if i not in unic_list:
            unic_list.append(i)
    print(unic_list)
    return words, unic_list


def sort(words):
    """
    creates list of starting words
    :param words: all words
    :return: list of starting words
    """
    capital = []
    for i in words:
        if i[0].isupper():
            capital.append(i)
    return capital


def choose(words):
    """
    chose random indexes
    :param words: all words
    :return: one random word
    """
    ind = random.randint(0, len(words) - 1)
    return words[ind]


def algorythm(connections, upper, sentences, uniq_words):
    """
    creates sentences
    :param connections: list of associations
    :param upper: list of capital words
    :param sentences: quantity of sentences
    :param uniq_words: list of uniq words
    :return: None
    """
    text = ''
    for first_layer in range(sentences):
        word = choose(upper)
        text += word + ' '
        words = connections[uniq_words.index(word)]
        for second_layer in range(19):
            word = choose(words)
            text += word + ' '
            words = connections[uniq_words.index(word)]
            if word[-1] in '.!?':
                break
        if text.rstrip()[-1] in string.punctuation:
            if not text.rstrip()[-1] in '.!?':
                text_copy = text[:-2]
                text = text_copy + '. '
        else:
            text = text.rstrip() + '. '
    print(text.rstrip())


d = start()
n = int(input('Введите количетво предложений: '))
d = re.sub(r'\s+(?=(?:[,.?!:;…]))', r'', d)
word, unic_word = unic(d)
u = sort(unic_word)

algorythm(associations(word, unic_word), u, 10, unic_word)
