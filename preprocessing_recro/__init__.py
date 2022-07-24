from  preprocessing_recro import utils

__version__ = '0.0.2'


def word_count(x):

   return 	utils._word_count(x)


def char_counts(x):
	
	return utils._char_counts(x)

def avg_word_count(x):
	return utils._avg_word_count(x)

def en_stopwords():
	utils._en_stopwords()


def en_stopwordscount(x):
	return  utils._uppercaseounts(x)


def hastagcount(x):
	return utils._hastagcount(x)


def mentioncount(x):
	return utils._mentioncount(x)

def digitcount(x):
	return utils._digitcount(x)
 


def uppercaseounts(x):
	return utils._uppercaseounts(x)

def cont_exp(x):
	return utils._cont_exp(x)

def getemails(x):
	

	return utils._getemails(x)


def remove_email(x):

	return utils._remove_email(x)
def  getulrs(x):
	
	return utils._getulrs(x)


def remove_urls(x):
	return utils._remove_urls(x)
def remove_rt(x):
	return utils._remove_rt(x)
def remove_specialchar(x):
	return utils._remove_specialchar(x)

def remove_htmltags(x):
	return utils._remove_htmltags(x)

def remove_accentedchars(x):
	return utils._remove_accentedchars(x)


def remove_stopwords(x):
	return utils._remove_stopwords(x)
def make_base(x):
	
	return utils._make_base(x)


def remove_common_words(x,n=20):
	
	return utils._remove_common_words(x,n=20)


def remove_rare_words(x,n=20):
	
	return utils._remove_rare_words(x,n=20)


def spelling_correction(x):
	return utils._spelling_correction(x)