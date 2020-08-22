import cantoseg

def test_cut():
    result = cantoseg.cut('香港喺舊石器時代就有人住')
    answer = ['香港', '喺', '舊石器時代', '就', '有人', '住']
    assert result == answer

def test_lcut():
    result = list(cantoseg.lcut('香港喺舊石器時代就有人住'))
    answer = ['香港', '喺', '舊石器時代', '就', '有人', '住']
    assert result == answer
