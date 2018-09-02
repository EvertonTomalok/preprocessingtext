name = 'emailtoolspython'
__author__ = 'Everton Tomalok'
__version__ = '0.0.1'
__email__ = 'evertontomalok123@gmail.com'

# !/usr/bin/env python3
# coding: utf-8

from textblob import TextBlob
import nltk
from string import punctuation


class CleanSentences:
    """
    Esta classe é designada ao pré-processamento do texto, para posterior análise do sentimento.

    Funções:
        => _tokenizer(self, words)
        => _removeStopWords(self, sentence)  ; sentence deve ser uma "STRING"
        => _removePunctuation(self, sentence)  ; sentence deve ser uma "STRING"
        => stemSetence(self, sentence="String", remove_stop_words = True, remove_punctuation= True)  ; sentence deve ser uma "STRING"

    """

    def __init__(self, idiom='portuguese'):
        """
        Starta a classe, stop words custom Portuguese, e também o stemmer do nltk
        """
        self.stopwords = nltk.corpus.stopwords.words(idiom)
        self.stemmer = nltk.stem.RSLPStemmer()

    def _tokenizer(self, words):
        """
        A String is received, and an array of tokens is returned.
        """

        if type(words) == list:
            words = ' '.join(words)
        tokens = TextBlob(words)

        tokens_return = []

        for prhase in tokens.words:
            tokens_return.append(prhase)

        return tokens_return

    def _remove_stop_words(self, sentence):
        """
        It receives a string, and removes the stop words (custom = portuguese) of the string, and return the result.
        """

        sentence = self._tokenizer(sentence)
        words_no_stop_words = [word.lower() for word in sentence if word.lower() not in self.stopwords]
        words_no_stop_words = ' '.join(words_no_stop_words)

        return words_no_stop_words

    def _remove_punctuation(self, sentence):
        """
        It receives a string, and removes the punctuation of the string, and return the result.
        """

        sentence = self._tokenizer(sentence)

        prhase_no_punc = [word for word in sentence if word not in punctuation]

        prhase_no_punc = ' '.join(prhase_no_punc)

        return prhase_no_punc

    def _replace_garbage_sentences(self, string):
        """
        A function to clean the string, removing tokens like http://, https://, etc.
        """

        list_to_replace = ['https://', 'http://', 'R$', '$', '’', ' brasil', ' Brasil']

        string_to_clean = string
        try:
            for item in list_to_replace:
                if item in string_to_clean:
                    string_to_clean = string_to_clean.replace(item, '')
        except Exception:
            pass

        return string_to_clean

    def stem_sentence(self, sentence='', remove_stop_words=True, remove_punctuation=True):
        """
            args=
                sentence: String
                remove_stop_words: Boolean
                remove_punctuation: Boolean

            A sentence needs to be passed as a string, and the parameters customs values of remove_stop_words and
            remove_punctuation is True, to remove the stop words and punctuation of the string.

            If you set one or both to False, you'll disable these functions.
        """
        if sentence == '':
            raise ValueError('A sentence needs to be passed as an argument.')

        if remove_punctuation is True:
            sentence = self._replace_garbage_sentences(sentence)
            sentence = self._remove_punctuation(sentence)

        if remove_stop_words is True:
            sentence = self._remove_stop_words(sentence)

        result = [self.stemmer.stem(word) for word in self._tokenizer(sentence)]

        result = ' '.join(result)

        return result
