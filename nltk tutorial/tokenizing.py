from nltk import word_tokenize , sent_tokenize

text = "Hello there, how are you? I am Mr.John. Python is awesome. It is definitely better than the Anaconda distribution!"


for sentence in sent_tokenize(text):
	print "SENTENCE------------>",sentence
	for word in word_tokenize(sentence):
		print word


#  stop words - Words that re irrelevant, that are not required for our desired analysis. ex: a, the, and, 

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = "This is an example sentence. But I don't know if this would work!"

stop_words = stopwords.words("english")
words = word_tokenize(sentence)
filtered_sentence = [w for w in words if w not in stop_words]

print "original sentence->", sentence
print "filtered sentence->", " ".join(filtered_sentence)	