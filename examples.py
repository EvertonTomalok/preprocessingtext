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

string_web = 'Acesse esses links para ganhar dinheiro: https://easymoney.com.net and http://falselink.com'
print(cleaner.stem_sentence(sentence=string_web,
                            remove_stop_words=False,
                            remove_punctuation=True,
                            replace_garbage=True
                            )
      )

en_cleaner = CleanSentences(idiom='english')
string_web = 'Access these links to gain money: https://easymoney.com.net and http://falselink.com'
print(en_cleaner.stem_sentence(sentence=string_web,
                            remove_stop_words=True,
                            remove_punctuation=True,
                            replace_garbage=True
                            )
      )
