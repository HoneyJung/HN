import nltk
from nltk.corpus import gutenberg
a = nltk.Text(gute
nberg.sents('austen-emma.txt'))
print(a)
b = [' '.join(i) for i in a for j in i if j.lower() == 'surprize']
print(b)

from nltk.corpus import gutenberg
>>> a = gutenberg.sents('austen-emma.txt')
>>> a[:2]
[['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']'], ['VOLUME', 'I']]
>>> b = [' '.join(i) for i in a for j in i if j.lower() == 'surprize']
>>> b[1:3]
['" You surprize me !', 'This was obliged to be repeated before it could be believed ; and Mr . Knightley actually looked red with surprize and displeasure , as he stood up , in tall indignation , and said ,']