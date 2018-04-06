from flask import json


class Parser():
    def __init__(self,language):
        self.language = language +".json"
        words_and_caracters = json.load(open(self.language))
        self.LIST_WORD = words_and_caracters["LIST_WORD"]
        self.LIST_CARACTER = words_and_caracters["LIST_CARACTER"]

    def parser(self, text):
        text_list = text.lower().split()
        number_list_word = 0
        word_is_remove = False
        while number_list_word != len(text_list):
            word_of_the_list = str(text_list[number_list_word])
            for caracter in self.LIST_CARACTER:
                if caracter not in word_of_the_list:
                    if word_of_the_list in self.LIST_WORD:
                        if word_of_the_list in text_list:
                            text_list.remove(word_of_the_list)
                            word_is_remove = True

                else:
                    word2 = word_of_the_list.split(caracter)
                    for word3 in word2:
                        if word3 in self.LIST_WORD or word_of_the_list in self.LIST_CARACTER:
                            if word_of_the_list in text_list:
                                text_list.remove(word_of_the_list)
                                word_is_remove = True

            if word_is_remove is False:
                number_list_word += 1
            else:
                word_is_remove = False
        return " ".join(text_list)

    def parser_refine(self, text):
        text_list = text.lower().split()
        text_list.pop(0)

        return " ".join(text_list)
