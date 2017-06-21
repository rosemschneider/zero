#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to cycle through corpora and create large corpora
"""

#Things that need to be done:
    #cycle through a small amount of the corpus at a time
    #write that with pertinent metadata to a csv, I think
    #clear memory, return to beginning of loop
    
#Preliminaries    
#import nltk
#import analysis
#from nltk.corpus.reader import CHILDESCorpusReader
#corpus_root = nltk.data.find('corpora/CHILDES/Eng-NA')
#
##just for starters, let's do the brown and bloom
#brown = CHILDESCorpusReader(corpus_root, 'Brown/.*.xml')
#bloom = CHILDESCorpusReader(corpus_root, 'Bloom70/.*.xml')


#list of corpora to be used 
#temp commented out
#corp_list = ['Bates', 'Gathercole', 'Peters', 'Belfast',			
#             'Gillam',	 'Post', 'Bernstein',	'Gleason', 'Providence', 
#             'Bliss',	'HSLLD', 'Rollins', 'Bloom70', 'Haggerty', 'Sachs',
#             'Bloom73', 'Hall', 'Sawyer', 'Bohannon', 'Higginson', 'Snow',
#             'Braunwald', 'Howe', 'Soderstrom', 'Brent', 	'Korman', 'Sprott',
#             'Brown',	'Kuczaj', 'Suppes', 'Clark', 'Lara', 'Tardif', 
#             'Cornell', 'MPI-EVA-Manchester', 'Thomas', 
#             'Cruttenden', 'MacWhinney', 'Tommerdahl',
#             'Davis',	'Manchester',	'Valian', 'Demetras1',	 'McMillan',		
#             'VanHouten' 'ErvinTripp', 'Morisset', 'VanKleeck',
#             'Fletcher', 'NH', 'Warren', 'Forrester', 'Nelson'	, 'Weist',
#             'Garvey', 'NewEngland', 'Wells', 'Gathburn', 'Normal']

#corp_list = ['Bloom70', 'Brown', 'Bates', 'Snow']

import os
import nltk
from childes import CHILDESCorpusReader
from unicode_csv import *

def get_corpus_reader(language):
    return CHILDESCorpusReader(corpus_root, r'%s.*/.*\.xml' % language[:3].title())

# Takes a fileid, gets counts of all the words for that file, writes a csv
def get_file_counts(corpus_reader, corpus_file, meta_writer, language):
    base_directory = os.path.dirname(corpus_file)
    directory = os.path.join('data', base_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    base_file = os.path.join(base_directory, os.path.basename(corpus_file).split('.xml')[0])
    filename = os.path.join('data', base_file + '.csv')
    if os.path.isfile(filename):
        print "Count file for %s already exists, skipping" % corpus_file
    else:
        print "Getting counts for %s" % corpus_file
        sex = corpus_reader.sex(corpus_file)[0]
        age = corpus_reader.age(corpus_file, month=True)[0]
        meta_writer.writerow([language, base_file, str(sex), str(age)])
        corpus_participants = corpus_reader.participants(corpus_file)[0]
        not_child = [value['id'] for key, value in corpus_participants.iteritems() if key != 'CHI']
        corpus_words = corpus_reader.words(corpus_file, speaker=not_child, replace=True, stem=False)
        freqs = nltk.FreqDist(corpus_words)
        writer = UnicodeWriter(open(filename, 'w'))
        writer.writerow(["word", "count"])
        for word, count in freqs.iteritems():
            try:
                writer.writerow([word, str(count)])
            except:
                print "couldn't write word %s with count %d" % (word, count)

languages = ["English"]
corpus_root = nltk.data.find('corpora/childes/data-xml')
meta_writer = UnicodeWriter(open('data/metadata.csv', 'a'))
meta_writer.writerow(["language", "filename", "sex", "age"])
for language in languages:
    corpus_reader = get_corpus_reader(language)
    for f in corpus_reader.fileids():
        get_file_counts(corpus_reader, f, meta_writer, language)











def readCorpus(corp_list):
    for i in corp_list:
        corpus_dir = i + '/.*.xml'
        corpus = CHILDESCorpusReader(corpus_root, corpus_dir)
        #get production vs. reception
        
    return corpus
        


def createCorpus():
    