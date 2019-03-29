import re

def get_words_from_text(text):
    return re.findall(r'\b\w+\b', text.lower())
