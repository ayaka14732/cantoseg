from collections import Counter
from os import path
import pycantonese as pc

HERE = path.abspath(path.dirname(__file__))

corpus = pc.hkcancor()
c = Counter()

for word, pos, _, _ in corpus.tagged_words():
    if pos.isalpha():
        c[word, pos.lower()] += 1

with open(path.join(HERE, 'dict_cantonese.txt'), 'w', encoding='utf8') as f:
    for (word, pos), freq in c.most_common():
        print(word, freq, pos, file=f)
