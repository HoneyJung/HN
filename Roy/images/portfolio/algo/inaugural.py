import nltk
from nltk.corpus import inaugural
from nltk.corpus import PlaintextCorpusReader
print(inaugural.fileids()[:5])
print([fileid[:4] for fileid in inaugural.fileids()])
#print(type(inaugural.fileids()[0]))
cfd = nltk.ConditionalFreqDist((target, fileid[:4])
for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
        for target in ['america', 'citizen']
            if w.lower().startswith(target))

print(cfd.plot())
#path = 'c:/05_test'
path = 'C:/Users/kinkin21c/Desktop/05_test'
wordlists = PlaintextCorpusReader(path, '.*')
print(wordlists.fileids())
wordlists = PlaintextCorpusReader(path, '^h.+')
print(wordlists.fileids()) # 정규표햔