from nltk.corpus import wordnet

syns = []
ants = []

for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		syns.append(l.name())
		if l.antonyms():
			ants.append(l.antonyms()[0].name())

print set(syns)
print set(ants)



w1 = wordnet.synset("ship.n.01") # noun and the first one
w2 = wordnet.synset("boat.n.01")

print w1.wup_similarity(w2)