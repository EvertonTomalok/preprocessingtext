from preprocessingtext import CleanSentences

cleaner = CleanSentences(idiom='portuguese')

string = "Eu sou uma sentença comum. Serei pré-processada com este módulo, veremos a seguir usando os métodos disponiveis"

#########################################################################################################################
# Removing stop words, punctuation, replacing some things in the string like http:// and https://, and normalizing text #
#########################################################################################################################

print(cleaner.stem_sentence(sentence=string,
                            remove_stop_words=True,
                            remove_punctuation=True,
                            normalize_text=True,
                            replace_garbage=True
                            )
      )

print(cleaner.stem_sentence(sentence=string,
                            remove_stop_words=False,
                            remove_punctuation=True,
                            normalize_text=True,
                            replace_garbage=True
                            )
      )

print(cleaner.tokenizer('Um exemplo de tokens.'))

