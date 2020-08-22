# cantoseg ![](https://github.com/ayaka14732/cantoseg/workflows/Python%20package/badge.svg)

Cantonese segmentation tool 粵語分詞工具

## Install

```sh
$ pip install cantoseg
```

## Usage

```python
>>> import cantoseg
>>> cantoseg.cut('香港喺舊石器時代就有人住')
['香港', '喺', '舊石器時代', '就', '有人', '住']
```

A generator version is also available: `cantoseg.lcut`.

## Design

See article [_Cantonese Segmentation and Part-Of-Speech Tagging_](https://ayaka.shn.hk/yueseg/hant/) (in Chinese).
