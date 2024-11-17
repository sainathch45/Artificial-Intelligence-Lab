# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zoowcjsFQ6aEaa_wtzq_ik0PFgSY8ZnS
"""

import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue.
You should\'t eat cardboard"""

sent=nltk.sent_tokenize(text)
print(sent)

import re
#text="SaaaMMM"
print(text.lower())
text=re.sub(r"[^a-z\'A-Z]", " ",text.lower())
text

words=text.split()
print(words)

from nltk.corpus import stopwords
print(stopwords.words("english"))

words= [w for w in words if w not in stopwords.words("english")]
print(words)

from nltk.stem.porter import PorterStemmer
stemmed=[PorterStemmer().stem(w) for w in words]
print(stemmed)

from nltk.stem.wordnet import WordNetLemmatizer
lemmed=[WordNetLemmatizer().lemmatize(w) for w in words]
print(lemmed)

from nltk import pos_tag,RegexpParser
tagged=pos_tag(lemmed)
print(tagged)
for i, (word,tag) in enumerate(tagged):
  if word=="weather":
    tagged[i]= (word,"NN")
  if word=="eat":
    tagged[i]=(word,"VB")
chunker=RegexpParser("""
NP:{}
P:{}
V:{}
PP:{}
VP:{}
""")
output=chunker.parse(tagged)
print("After Extracting",output)

nltk.download('averaged_perceptron_tagger_eng')

