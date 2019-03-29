from collections import Counter
from split_text import get_words_from_text

WORDS = Counter(get_words_from_text(open('./big_data/russian_data.txt').read()))
LETTERS = "абвгдеёжзийклмнопстуфхцчшщъыьэюя"
DEPTH = 2

def most_probably_word(word, words_count=sum(WORDS.values())):
    try:
        return WORDS[word] / words_count
    except ZeroDivisionError:
        print('There is no words')

def get_correct_word(word, lang, depth):
    global WORDS, LETTERS, DEPTH
    DEPTH = depth
    if lang == 'en':
        WORDS = Counter(get_words_from_text(open('./big_data/english_data.txt').read()))
        LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    elif lang == 'ru':
        WORDS = Counter(get_words_from_text(open('./big_data/russian_data.txt').read()))
        LETTERS = "абвгдеёжзийклмнопстуфхцчшщъыьэюя"
    else:
        return 'unknown language'
    return max(get_probably_words(word), key=most_probably_word)

def get_probably_words(word):
    return (get_words_from_big_data([word]) or get_words_from_big_data(get_edited_words(word))
        or make_strong_search(word) or [word])

def get_words_from_big_data(words):
    return set(word for word in words if word in WORDS)

def get_edited_words(word):
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in LETTERS]
    inserts    = [L + c + R               for L, R in splits for c in LETTERS]
    return set(deletes + transposes + replaces + inserts)

def make_strong_search(word):
    again_edited_words = (w2 for w1 in get_edited_words(word) for w2 in get_edited_words(w1))
    for i in range(DEPTH):
        words = get_words_from_big_data(again_edited_words)
        if words:
            return words
        again_edited_words = (edited_word for word in again_edited_words for edited_word in get_edited_words(word))
    return []
