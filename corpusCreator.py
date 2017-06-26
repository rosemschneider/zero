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


#check to make sure all files actually came in


#now I want to make a dataframe
#what needs to be in the df: 
    #sentences with the targeted words
    #associated ages
    #associated mlu
    #associated corpus
        #this needs to be done with a for loop
#I want two sep. dfs - one for reception and one for production

    

