import os
import re
import unidecode
from flask import json

"""
The parser class takes as parameter for the construction of the object the text language 
which will be parser which will be parser. Example : Parser = Parser('fr'). 
Languages can be found and created in the same folder as the package. 
"""


class Parser:
    def __init__(self, language):
        file_dir_path = os.path.dirname(os.path.abspath(__file__))
        self.language = os.path.join(file_dir_path + "/{}.json".format(language))
        words_and_caracters = json.load(open(self.language))
        self.LIST_WORD = words_and_caracters["LIST_WORD"]

    # Function that will parse the text
    def parser_word(self, text):

        text_list = unidecode.unidecode(text.lower())
        text_list = re.split(r"[^a-zA-Z0-9]", text_list)
        number_list_word = 0
        word_is_remove = False

        while number_list_word != len(text_list):
            word_of_the_list = str(text_list[number_list_word])

            if word_of_the_list in self.LIST_WORD:
                if word_of_the_list in text_list:
                    text_list.remove(word_of_the_list)
                    word_is_remove = True

            if word_is_remove is False:
                number_list_word += 1
            else:
                word_is_remove = False
        return " ".join(text_list)
