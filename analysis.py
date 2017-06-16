#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:47:45 2017

@author: rschneid

Code for loading corpora
"""
import os
import glob
import re
import pandas as pd
#os.chdir('/Users/rschneid/Documents/Projects/zero')
os.chdir('/Users/roseschneider/Documents/Projects/zero')

import textSearch
import textStats

#create number text and parse files
textSearch.find_nums_to_ten('input/input.txt')
textSearch.find_nums_teens('input/input.txt')
textSearch.find_nums_decades('input/input.txt')
textSearch.find_nums_large('input/input.txt')

##open files

def readFiles(fname):
    array = []
    for filename in glob.glob(fname):
        with open(filename, 'r+', encoding = 'latin1') as file_open:
            array.append(file_open.read())
    return array       
            
num_text = readFiles('parse_tag_out/search/*.txt') 
num_text = str(num_text)
num_text = textStats.corpusClean(num_text) 

#get type frequencies and make a bar plot of number word frequencies
def freq_analysis(txt):
    import re
    freqs = textStats.getTypeFreq(txt)
    num_freqs = textStats.getSpec(freqs, ('zero', 'one', 'two', 'three', 'four', 
                                'five', 'six', 'seven', 'eight', 'nine',
                                'ten', 'eleven', 'twelve', 'thirteen', 
                                'fourteen', 'fifteen', 'sixteen', 'seventeen',
                                'eighteen', 'nineteen', 'twenty', 'thirty',
                                'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                                'ninety', 'hundred', 'thousand', 'million', 'trillion', 'billion'))
    textStats.makeBar(num_freqs)
    
freq_analysis(num_text)  

##get tag frequencies and make a bar plot

#first tag sentences
textSearch.tag_sents('num_to_ten', 'num_to_ten')
#os.chdir('/Users/rschneid/Documents/Projects/zero')
os.chdir('/Users/roseschneider/Documents/Projects/zero')
textSearch.tag_sents('num_teens', 'num_teens')
#os.chdir('/Users/rschneid/Documents/Projects/zero')
os.chdir('/Users/roseschneider/Documents/Projects/zero')
textSearch.tag_sents('num_decades', 'num_decades')
#os.chdir('/Users/rschneid/Documents/Projects/zero')
os.chdir('/Users/roseschneider/Documents/Projects/zero')
textSearch.tag_sents('num_large', 'num_large')
#os.chdir('/Users/rschneid/Documents/Projects/zero')
os.chdir('/Users/roseschneider/Documents/Projects/zero')

#read in those files
num_tags = readFiles('parse_tag_out/tag/*.txt')
num_tags = str(num_tags)

freqs = textStats.getTypeFreq(num_tags)

def tag_freq_analysis(di, substr):
    new = []
    for s in substr:
        for key, value in di.items():
            if key.startswith(s):
                new.append((key, value))
    new = dict(new)
    return new         

num_tags_ten = tag_freq_analysis(freqs, ('one_', 'two_', 'three_', 
                                         'four_', 'five_', 'six_', 
                                         'seven_', 'eight_', 'nine_', 'zero_'))
num_tags_decades = tag_freq_analysis(freqs, ('zero_', 'twenty_', 'thirty_', 
                                             'forty_', 'fifty_', 'sixty_', 
                                             'seventy_', 'eighty_', 'ninety_'))
num_tags_large = tag_freq_analysis(freqs, ('zero_', 'hundred_', 'thousand_', 
                                           'million_', 'billion_', 'trillion_'))
num_tags_teens = tag_freq_analysis(freqs, ('zero_', 'eleven_', 'twelve_', 'thirteen_', 
                                           'fourteen_', 'fifteen_', 'sixteen_', 
                                           'seventeen_', 'eighteen_', 'nineteen_'))

textStats.makeBar(num_tags_ten)
textStats.makeBar(num_tags_decades)
textStats.makeBar(num_tags_teens) 
textStats.makeBar(num_tags_large)

###bigram analysis
#first get the bigrams
bigrams = textStats.getWordnGrams(num_text, 2)

#next, filter down to only number word bigrams
#this is for ALL number words, but it's rather large, so see below for up to ten, etc.
filter_set = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
              'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
              'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 
              'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred'
              'thousand', 'million', 'billion', 'trillion']

##THIS does not work - have to figure out why later
##THE PLAN: I want to get only number-number bigrams, make confusion matrix
##Next, I want to get top 10 most frequent bigrams for each number word
tuples_filtered = (([tup for tup in bigrams if tup[0] in filter_set]) & ([tup for tup in bigrams if tup[1] in filter_set]))

#up to ten (including zero)
def getExactNgrams(dataset, filter_set):
    ngrams_filtered = []
    ngrams_filtered = ([tup for tup in dataset if tup[0] in filter_set and tup[1] in filter_set])
    ngrams = textStats.getFreq(ngrams_filtered)
    ngrams = dict(textStats.sortFreqs(dict(ngrams)))
    return ngrams

if(t[0] in x or t[1] in x):
   print('????')

###The plan for below: 
    #now that we have some basics stats, the plan going forward is to dive into the corpora
    #step 1 is to compile the appropriate corpora
    #split by production and reception
    #mak a graph of prod/recep by age for zero (and none)
    #intensive corpus analysis: brown, providence, manchester - look at how zero is used, when it's said
    
#First, create the large corpus

#Pull out the Brown, Providence, and Manchester corpora
import nltk
from nltk.corpus.reader import CHILDESCorpusReader
corpus_root = nltk.data.find('corpora/CHILDES/Eng-NA')

brown = CHILDESCorpusReader(corpus_root, 'Brown/.*.xml')
sarah = [f for f in brown.fileids() if f[6:11] == 'Sarah']
adam = [f for f in brown.fileids() if f[6:10] == 'Adam']
eve = [f for f in brown.fileids() if f[6:9] == 'Eve']

#create key for matching fileid with age and MLU
def createKey(corpus):
    age = brown.age(corpus)
    fileids = eve
    mlu = brown.MLU(corpus)
    corpus_key = zip(fileids, age, mlu)
    return list(corpus_key)

sarah_key = createKey(sarah)
adam_key = createKey(adam)
eve_key = createKey(eve)

#read the sentences, export to txt file
eve_sents_child = brown.sents(eve, speaker = 'CHI')

def createCorpus(main_corpus, child, participant):
    sents = []
    age = []
    mlu = []
    fileid = []
#    key = createKey(child)
    for i in child:
        fileid.append(i)
        age.append(str(brown.age(i)))
        utterance = str(main_corpus.sents(i, speaker = participant))
        sents.append(textStats.corpusClean(utterance))
        mlu.append(brown.MLU(i))
    corpus = zip(fileid, age, mlu, sents) 
#    what I need to do here is convert the sentences to text and run the corpus cleaner on them
    corpus = list(corpus)
#    for i in corpus:
#        i[3] = str(i[3])
    return corpus

##now make a dataframe for that corpus
#goal is to have this function also convert everything to appropriate format
def makeDF(lst):
    df = pd.DataFrame(lst, columns = ['fileid', 'age', 'mlu', 'sentences'])
    return df

#now get types and frequencies
def dfTypeFreq(df, column):
    all_counts = []
    counts = dict()
    for i in df[column]:
        string = str(i)
        toks = textStats.getTokens(string)   
        freqs = textStats.getTypeFreq(str(toks))
        all_counts.append(freqs)
    return all_counts

def cleanDict(lst):
    #inputs a list of dictionaries to remove special characters
    clean = []
    symbols = ["'", ',', '[', ']']
    for i in lst:
        for s in symbols:
            clean.append(i.pop(s, None))
    return lst

##okay so I have type frequencies - let's do this for all the kids in the corpus
eve_corpus_child = makeDF(createCorpus(brown, eve, 'CHI'))
eve_corpus_mot = makeDF(createCorpus(brown, eve, 'MOT'))
adam_corpus_child = makeDF(createCorpus(brown, adam, 'CHI'))
adam_corpus_mot = makeDF(createCorpus(brown, adam, 'MOT'))
sarah_corpus_child = makeDF(createCorpus(brown, sarah, 'CHI'))
sarah_corpus_mot = makeDF(createCorpus(brown, sarah, 'MOT'))

#frequencies
def freqDF(lst):
    age = []
    mlu = []
    fileid = []
    freqs = []
#    key = createKey(child)
    for i in lst:
        fileid.append(i)
        age.append(str(brown.age(i)))
        freqs.append(i)
        mlu.append(brown.MLU(i))
    corpus = zip(fileid, age, mlu, freqs) 
#    what I need to do here is convert the sentences to text and run the corpus cleaner on them
    corpus = list(corpus)
#    for i in corpus:
#        i[3] = str(i[3])
    return corpus





eve_child_freqs = cleanDict(dfTypeFreq(eve_corpus_child, 'sentences'))
eve_mother_freqs = zip(eve_key, cleanDict(dfTypeFreq(eve_corpus_mot, 'sentences')))

#now search for zero


#need to figure out dataframe here
#to get the sentences into a string: str(sents[i][j]), then run corpus clean on that




        
    
   

 
