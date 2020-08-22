# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

if not path.exists(path.join(here, 'src/cantoseg/merged_dict.txt')):
    raise Exception('Please run the three Python scripts in build directory first.')

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

with open(path.join(here, 'src/cantoseg/version.py'), encoding='utf8') as f:
    exec(f.read())

setup(
    name='cantoseg',
    version=__version__,
    description='Cantonese segmentation tool 粵語分詞工具',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ayaka14732/cantoseg',
    author='ayaka14732',
    author_email='ayaka@mail.shn.hk',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Cantonese',
        'Natural Language :: Chinese (Traditional)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='cantonese chinese natural-language-processing',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'cantoseg': ['merged_dict.txt'],
    },
    include_package_data=True,
    python_requires='>=3.5, <4',
    install_requires=['jieba'],
    entry_points={},
    project_urls={
        'Bug Reports': 'https://github.com/ayaka14732/cantoseg/issues',
        'Source': 'https://github.com/ayaka14732/cantoseg',
    },
    zip_safe=False
)
