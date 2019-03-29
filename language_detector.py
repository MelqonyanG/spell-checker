
def is_english(word):
    for letter in word:
        val = ord(letter)
        if letter.isalpha() and not (65 <= val <= 90 or 97 <= val <= 122):
            return False
    return True

def is_russian(word):
    for letter in word:
        val = ord(letter)
        if letter.isalpha() and not (1040 <= val <= 1103):
            return False
    return True

def detect_language(word):
    if is_english(word):
        return 'en'
    if is_russian(word):
        return 'ru'
    return 'unknown'
