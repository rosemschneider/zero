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
os.chdir('/Users/rschneid/Documents/Projects/zero')

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
os.chdir('/Users/rschneid/Documents/Projects/zero')
textSearch.tag_sents('num_teens', 'num_teens')
os.chdir('/Users/rschneid/Documents/Projects/zero')
textSearch.tag_sents('num_decades', 'num_decades')
os.chdir('/Users/rschneid/Documents/Projects/zero')
textSearch.tag_sents('num_large', 'num_large')
os.chdir('/Users/rschneid/Documents/Projects/zero')

#read in those files
num_tags = readFiles('parse_tag_out/tag/*.txt')
num_tags = str(num_tags)

freqs = textStats.getTypeFreq(num_tags)
test = textStats.getTags(freqs, ('one', 'two'))

def tag_freq_analysis  