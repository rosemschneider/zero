# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk

from nltk.corpus.reader import CHILDESCorpusReader

corpus_root = nltk.data.find('corpora/CHILDES/Eng-NA')


#first, create the conglomerate english (NA) corpus
eng_na_corpus = CHILDESCorpusReader(corpus_root, '.*.xml')

#then create the conglomerate english (UK) corpus
corpus_root = nltk.data.find('corpora/CHILDES/Eng-UK')
eng_uk_corpus = CHILDESCorpusReader(corpus_root, '.*.xml')

#create the merged english corpus
merged_eng = eng_na_corpus.fileids() + eng_uk_corpus.fileids()

#check to make sure all files actually came in
assert len(x) > 0, 'No files here'



