# preprocessingtext
<br>
A tool short, but very usefull to help in pre-processing data from texts.

<br>

## How to Install
<br>

    >> pip install --user preprocessingtext
    
<br>

## Usage

    >> from preprocessingtext import CleanSentence
    
    >> cleaner =  CleanSentence(idiom='portuguese')
    
    >> cleaner.stem_sentence(sentence="String", remove_stop_words=True, remove_punctuation=True)

To init a a class, you need to pass the idiom that you want to work. The custom value, is "portuguese".<br><br>

Before, you can instance a new object from CleanSentence, and call the method stem_sentence. You can choose in use 
"remove_stop_words" from string (pass True or False) and "remove_punctuation" from string (pass True or False).

## Example

    >> string = "Eu sou uma sentença comum. Serei pré-processada com este modulo, veremos a serguir usando os métodos disponiveis"
    
    >> cleaner.stem_sentence(sentence=string,
                            remove_stop_words=True,
                            remove_punctuation=True,
                            normalize_text=True,
                            replace_garbage=True
                            )
       
    >> sentenc comum pre-process modul ver segu us metod disponi
    
    >> print(cleaner.stem_sentence(sentence=string,
                            remove_stop_words=False,
                            remove_punctuation=True,
                            normalize_text=True,
                            replace_garbage=True
                            )
      )
      
    >> eu sou uma sentenc comum ser pre-process com est modul ver a segu us os metod disponi

<br><br><br>
# Author
{
<br>'name': Everton Tomalok,<br>
'email': evertontomalok123@gmail.com<br>
}