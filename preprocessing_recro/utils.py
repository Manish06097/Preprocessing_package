import re
import os
import sys
import pandas as pd
import numpy as np

import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob	

def _word_count(x):

   return len(str(x).split())	


def _char_counts(x):
	s=str(x).split()
	x="".join(s)
	return len(x)

def _avg_word_count(x):
	return _char_counts(x)/_word_count(x)

def _en_stopwords():
	print (stopwords)


def _en_stopwordscount(x):
	return len([t for t in x.split() if t in stopwords])


def _hastagcount(x):
	return len([t for t in x.split() if t.startswith("#")])


def _mentioncount(x):
	return len([t for t in x.split() if t.startswith("@")])

def _digitcount(x):
	return len([t for t in x.split() if t.isdigit()])
 


def _uppercaseounts(x):
	return len([t for t in x.split() if t.isupper()])

def _cont_exp(x):
	contractions = { 
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how does",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
" u ": " you ",
" ur ": " your ",
" n ": " and ",
"won't": "would not",
'dis': 'this',
'bak': 'back',
'brng': 'bring'}



	if type(x) is str:
		for key in contractions:
			value = contractions[key]
			x = x.replace(key, value)
		return x
	else:
		return x



def _getemails(x):
	emails= re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)',x)

	counts=len(emails)

	return counts,emails


def _remove_email(x):

	return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

def  _getulrs(x):
	urls=re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)
	counts=len(urls)
	return counts,urls


def _remove_urls(x):
	return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

def _remove_rt(x):
	return re.sub(r'\brt\b','',x).strip()

def _remove_specialchar(x):
	return ' '.join((re.sub(r'[^\w ]+', "", x)).strip())

def _remove_htmltags(x):
	return BeautifulSoup(x, 'lxml').get_text().strip()


def _remove_accentedchars(x):
	x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	return x


def _remove_stopwords(x):
	return ' '.join([t for t in x.split() if t not in stopwords])

def _make_base(x):
	nlp = spacy.load('en_core_web_sm')
	x = str(x)
	x_list = []
	doc = nlp(x)
	
	for token in doc:
		lemma = token.lemma_
		if lemma == '-PRON-' or lemma == 'be':
			lemma = token.text

		x_list.append(lemma)
	return ' '.join(x_list)

def _value_counts(df,col):
	text = ''.join(df[col])
	text=text.split()
	freq = pd.Series(text).value_counts()
	fn = freq

def _remove_common_words(x,freq,n=20):
	
	fn = freq[:n]
	return ' '.join([t for t in x.split() if t not in f20])


def _remove_rare_words(x,freq,n=20):
	
	fn = freq.tail(n)
	return ' '.join([t for t in x.split() if t not in f20])


def _spelling_correction(x):
	return TextBlob(x).correct()