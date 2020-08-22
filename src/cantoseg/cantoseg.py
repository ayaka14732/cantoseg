import jieba
import logging
from os import path

HERE = path.abspath(path.dirname(__file__))

jieba.setLogLevel(logging.INFO)
jieba.set_dictionary(path.join(HERE, 'merged_dict.txt'))
jieba.initialize()

import jieba.posseg as pseg

def lcut(s):
    return (w.word for w in pseg.lcut(s))

def cut(s):
    return list(lcut(s))
