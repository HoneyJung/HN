import re
from nltk.corpus import gutenberg
from nltk.corpus import brown
import nltk

print("brown.categories())")
print(brown.categories())
print("brown.words(categories = 'news')")
print(brown.words(categories = 'news'))
print("len(brown.words(categories='news'))")
print(len(brown.words(categories='news')))
print("len(brown.words(categories='editorial'))")
print(len(brown.words(categories='editorial')))
print("len(brown.words(categories=['news', 'editorial']))")
print(len(brown.words(categories=['news', 'editorial'])))
print("brown.words(fileids=['cg22', 'cg21'])")
print(brown.words(fileids=['cg22', 'cg21']))
print("len(brown.words(fileids=['cg22', 'cg21']))")
print(len(brown.words(fileids=['cg22', 'cg21'])))
######################################################################################################


words = brown.words(categories=['news', 'editorial'])
print("Freq = nltk.FreqDist(w.lower() for w in words)")
Freq = nltk.FreqDist(w.lower() for w in words)
print((Freq))

modals = ['can', 'could', 'may', 'might', 'must', 'will']
for i in modals:
    print(i + ':', Freq[i])


#print(len(brown.words(categories='humor')))
######################################################################################################
cfd = nltk.ConditionalFreqDist(('humor',word) for word in brown.words(categories='humor'))
print(cfd.plot())
######################################################################################################
genres = ['news', 'religion', 'hobbies']
modals = ['can', 'could', 'may', 'might']
print(cfd.tabulate(conditions=genres, samples=modals))