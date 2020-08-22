from os import path
from urllib import request

HERE = path.abspath(path.dirname(__file__))
DICT_URL = 'https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big'
PATH = path.join(HERE, 'dict.big.txt')

if not path.exists(PATH):
    request.urlretrieve(DICT_URL, PATH)
