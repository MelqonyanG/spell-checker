import argparse
from language_detector import detect_language
from spell_checker import get_correct_word
from split_text import get_words_from_text

DEFAULT_TEXT = '''
        Пришло теплое лето. На лисной опушки распускаюца колоколчики, незабутки, шыповник.
        Белые ромашки пратягивают к сонцу свои нежные лепески.
        Вылитают из уютных гнёзд птинцы. У зверей взраслеет смена. Мидвежата старше всех.
       '''

DEFAULT_SEARCHING_DEPTH = 2

def spell_checker(text, depth):
    words = get_words_from_text(text)
    incorrect_words = []
    for word in words:
        lang = detect_language(word)
        if lang != 'unknown':
            correct_word = get_correct_word(word, lang, depth)
            if correct_word != word:
                incorrect_words.append(word + " - " + correct_word)
    return incorrect_words

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-text', type=str, default=DEFAULT_TEXT,  help='Enter Text')
    parser.add_argument('-depth', type=int, default=DEFAULT_SEARCHING_DEPTH,  help='Enter Depth')
    args = parser.parse_args()
    text = args.text
    depth = args.depth
    print(spell_checker(text, depth))
