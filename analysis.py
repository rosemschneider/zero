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
tuples_filtered = [tup for tup in bigrams if tup[0] in filter_set] + [tup for tup in bigrams if tup[1] in filter_set]

#up to ten (including zero)
filter_set = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
              'nine', 'ten']
ten_bigrams_filtered = [tup for tup in bigrams if tup[0] in filter_set] + [tup for tup in bigrams if tup[1] in filter_set]
ten_bigram_freqs = textStats.getFreq(ten_bigrams_filtered)
textStats.makeBar(ten_bigram_freqs)

 
