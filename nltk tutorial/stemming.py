# stemming is the process of extracting the base word 
# i was taking a ride in the car
# i was riding in the car
#  the base word is "ride"

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# words = ["python", "pythoning", "pythoner", "pythoned", "pythonly"]
# for w in words:
# 	print ps.stem(w)

sentence = "It is very important to speak correctly when you are giving a speech. Professors should always keep that in mind."
stemmed_sentence = " ".join([ps.stem(w) for w in word_tokenize(sentence)])

print stemmed_sentence