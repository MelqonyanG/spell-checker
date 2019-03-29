# spell-checker

spell-checker is an application for finding the wrong words and correcting them in text written in Russian or English.
## Features

  - You can set English or Russian text to check.
  - You can set a depth for word checking.
 ### Tech
* Python3
* collections, re, argparse (Python standard libs)

### Modules

* main.py - The main module, that accepts text and/or depth (with arguments -text and -depth) successively checks and corrects words from text.
* split_text.py - The split module returns all words from the specified text.
* language_detector.py - The language_detector module returns the language of the word, because this application can receive texts in English or Russian.
* spell_checker.py - The spell_checker module gets the word, language and depth. This module searches for a word in big data and edits it, if necessary, in accordance with the depth. Then returns the correct word.

 ### Using
Default text and default depth are defined in the main module:
```sh
DEFAULT_TEXT = '''
        Пришло теплое лето. На лисной опушки распускаюца колоколчики, незабутки, шыповник. Белые ромашки пратягивают к сонцу свои нежные лепески. Вылитают из уютных гнёзд птинцы. У зверей взраслеет смена. Мидвежата старше всех.
       '''
```

```sh
DEFAULT_SEARCHING_DEPTH = 2
```

If you want to check the default text with the default depth, you must run the following command:
```sh
    python3 main.py
```

If you want to check your text with the default depth, you must define your text with **-text** parameter by running the following command:
```sh
    python3 main.py -text 'write your text in quotes'
```

If you want to check default text with your wanted depth, you must define your depth with **-depth** parameter by running the following command:
```sh
    python3 main.py -depth 3
```
If you want to check your wanted text with your wanted depth, you must define necessary text with parameter **-text** and necessary depth with **-depth** parameter by running the following command:
```sh
    python3 main.py -text 'write your text in quotes' -depth 3
```
