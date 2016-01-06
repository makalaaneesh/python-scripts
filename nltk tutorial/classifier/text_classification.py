import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = [w.lower() for w in movie_reviews.words()]
all_words = nltk.FreqDist(all_words)
# print all_words.most_common(15)


word_features = list(all_words.keys())[:3000] # first 3000 words. Can't have too many features

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features

print find_features(movie_reviews.words('neg/cv000_29416.txt'))

featuresets = [(find_features(rev), category) for (rev,category) in documents] # feature-set and desired output (y)


# naive bayes algo

training_set = featuresets[:1900] 
testing_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print "Naive bayes algo accuracy for training_set is", nltk.classify.accuracy(classifier, training_set)*100
print "Naive bayes algo accuracy for testing_set is", nltk.classify.accuracy(classifier, testing_set)*100


