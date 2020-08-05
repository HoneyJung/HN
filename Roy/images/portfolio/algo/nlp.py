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
#print(gutenberg.categories())
