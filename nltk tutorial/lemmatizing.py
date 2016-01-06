''' 
Something like stemming but will return an actual word
'''

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print lemmatizer.lemmatize("cats")
print lemmatizer.lemmatize("skies")
print lemmatizer.lemmatize("worrying")
print lemmatizer.lemmatize("catches")
print lemmatizer.lemmatize("singer")
print lemmatizer.lemmatize("lively", pos = "a")


print lemmatizer.lemmatize("better", pos ="a") # a for adjective



