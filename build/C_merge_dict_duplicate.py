from collections import Counter
from os import path

HERE = path.abspath(path.dirname(__file__))

# cmn

counter_cmn = Counter()

with open(path.join(HERE, 'dict.big.txt'), encoding='utf8') as f:
    for line in f:
        word, freq, tag = line.rstrip('\n').split(' ')
        counter_cmn[word, tag] += int(freq)

de_freq = counter_cmn['的', 'uj']

# yue

counter_yue = Counter()

with open(path.join(HERE, 'dict_cantonese.txt'), encoding='utf8') as f:
    for line in f:
        word, freq, tag = line.rstrip('\n').split(' ')
        counter_yue[word, tag] += int(freq)

ge_freq = counter_yue['嘅', 'u']

# merge

c = Counter()
w = de_freq / ge_freq

for k, v in counter_cmn.items():
    c[k] += v

for k, v in counter_yue.items():
    c[k] += round(v * w)

with open(path.join(HERE, '..', 'src', 'cantoseg', 'merged_dict.txt'), 'w', encoding='utf8') as f:
    for (word, pos), freq in c.most_common():
        print(word, freq, pos, file=f)
