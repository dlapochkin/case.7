import re, random, string

def start():
    with open(input('Введите имя файла')) as f_in:
        d = ''
        for line in f_in:
            r = line.strip()
            d += r + ' '
        return d
'''#Функция убирает пробелы до знаков препинания (a строка на вход - d а выход)
def whitespace(a):
    a= a.split()
    d = []
    print(a)
    for i in range(len(a)):

        if a[i] in '.,!-?':
            d[i-1] = d[i-1] + a[i]
        else:
            d.append(a[i])
    d = ' '.join(map(str, d))
    print(d)
    return d'''


def associations(raw, uniq):
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
    find unic words
    :param a:
    :return:
    """
    u = []
    b = a.split()
    for i in b:
        if i not in u:
            u.append(i)
    print(u)
    return b,u


def sort(b):
    z = []
    w = []
    for i in b:
        if i[0].isupper():
            z.append(i)
        else:
            w.append(i)
    print(z, w)
    return z, w


def choose(words):
    ind = random.randint(0, len(words)-1)
    return words[ind]


def algorythm(connections, upper, sentences, uniq_words):
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


d=start()
d=re.sub(r'\s+(?=(?:[,.?!:;…]))', r'', d)
words,unic_words = unic(d)
u, l = sort(unic_words)


algorythm(associations(words, unic_words), u, 10, unic_words)