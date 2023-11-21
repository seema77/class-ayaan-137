import nltk # natural lang toolkit

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

import json
import pickle
import numpy as np


words=[] #input #i am not feeling well
classes=[] #category
word_tags_list=[] # ["hi",greeting] [i am not feeling well, sad]
ignore_words=['?','!',',','.',"'s","'m"]
train_data_file=open('intents.json').read()
intents=json.loads(train_data_file)

def get_stem_words(words,ignore_words): #i'm not feeling well 
    stem_words=[]
    for word in words:
        if word not in ignore_words:
            w=stemmer.stem(word.lower())
            stem_words.append(w)
    return stem_words

for intent in intents['intents']:
    for pattern in intent['patterns']:
        pattern_word=nltk.word_tokenize(pattern) # "i","am","not","feeling","well"
        words.extend(pattern_word)
        word_tags_list.append((pattern_word,intent['tag']))
    if intent['tag'] not in classes:
        classes.append(intent['tag'])
        stem_words=get_stem_words(words,ignore_words)

print(words)
print("--------------------------------------------->")
print(stem_words)
