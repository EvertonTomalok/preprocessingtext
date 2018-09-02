# !/usr/bin/env python3
# coding: utf-8

from textblob import TextBlob
import nltk
from string import punctuation
from unicodedata import normalize

name = 'preprocessingtext'
__author__ = 'Everton Tomalok'
__version__ = '0.0.3'
__email__ = 'evertontomalok123@gmail.com'


class CleanSentences:
    """
    Esta classe é designada ao pré-processamento do texto, para posterior análise do sentimento.

    Funções:
        => tokenizer(self, words)
        => _remove_stop_words(self, sentence)  ; sentence deve ser uma "STRING"
        => _remove_punctuation(self, sentence)  ; sentence deve ser uma "STRING"
        => stem_setence(self, sentence="String", remove_stop_words = True, remove_punctuation= True)  ; sentence deve ser uma "STRING"

    """

    def __init__(self, idiom='portuguese'):
        """
        Starta a classe, stop words custom Portuguese, e também o stemmer do nltk

        :arg idiom: STRING
        """
        try:
            self.stopwords = nltk.corpus.stopwords.words(idiom)
        except LookupError:
            nltk.download('stopwords')
            self.stopwords = nltk.corpus.stopwords.words(idiom)

        # Stemmer que funciona bem com o português
        self.stemmer = nltk.stem.RSLPStemmer()

        self.list_to_replace = ['https://', 'http://', '$']

    def tokenizer(self, words):
        """
        A String is received, and an array of tokens is returned.

        :arg words: STRING

        :return List of words: LIST
        """

        if type(words) == list:
            words = ' '.join(words)

        tokens = TextBlob(words)

        tokens_return = [prhase for prhase in tokens.words]

        return tokens_return

    def _remove_stop_words(self, sentence):
        """
        It receives a string, and removes the stop words (custom = portuguese) of the string, and return the result.

        :arg sentence: STRING
        :return STRING
        """

        sentence = self.tokenizer(sentence)
        words_no_stop_words = [word.lower() for word in sentence if word.lower() not in self.stopwords]
        words_no_stop_words = ' '.join(words_no_stop_words)

        return words_no_stop_words

    def _remove_punctuation(self, sentence):
        """
        It receives a string, and removes the punctuation of the string, and return the result.

        :arg sentence: STRING
        :return STRING
        """

        sentence = self.tokenizer(sentence)

        prhase_no_punc = [word for word in sentence if word not in punctuation]

        prhase_no_punc = ' '.join(prhase_no_punc)

        return prhase_no_punc

    def _replace_garbage_sentences(self, string):
        """
        A function to clean the string, removing tokens like http://, https://, etc.

        :arg string: STRING
        :return STRING
        """

        string_to_clean = string
        try:
            for item in self.list_to_replace:
                if item in string_to_clean:
                    string_to_clean = string_to_clean.replace(item, '')
        except Exception:
            pass

        return string_to_clean

    def stem_sentence(self,
                      sentence='',
                      remove_stop_words=True,
                      remove_punctuation=True,
                      normalize_text=True,
                      replace_garbage=True):

        """
            :args :
                sentence: String
                remove_stop_words: Boolean
                remove_punctuation: Boolean
                normalize_text:Boolean
                replace_garbage:Boolean

            A sentence needs to be passed as a string, and the parameters customs values of remove_stop_words and
            remove_punctuation is True, to remove the stop words and punctuation of the string.
            normalize_text will remove accented characters.
            replace_garbage will remove http://, https://, $,  and you can replace or append new items in
            self.list_to_replace

        :return STRING
        """
        if sentence == '':
            raise ValueError('A sentence needs to be passed as an argument.')

        if replace_garbage:
            sentence = self._replace_garbage_sentences(sentence)

        if normalize_text:
            sentence = normalize('NFKD', sentence).encode('ASCII', 'ignore').decode("utf-8")

        if remove_punctuation:
            sentence = self._remove_punctuation(sentence)

        if remove_stop_words:
            sentence = self._remove_stop_words(sentence)

        result = [self.stemmer.stem(word) for word in self.tokenizer(sentence)]

        result = ' '.join(result)

        return result
