#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is an analysis script for individual utterances that have already been
compiled into a dataframe and are in csv form
"""

import os
import pandas as pd
import numpy
import re
import numpy as np

os.chdir('Documents/Projects/zero')

import textSearch
import textStats

#a function for reading in dfs
def readCSV(fname):
    df = pd.DataFrame.from_csv(fname)
    return df

df = readCSV('zero_search1.csv')

#frequencies by age
def freqsByAge(df):
    """This is a function to return the number of utterances a given word 
    by age."""
    empty_col = []   
    for row in df['utterance']:
        empty_col.append(textStats.getTypeFreq(row))
    freqs = pd.Series(empty_col)
    #need to convert series to df to append
    freqs = freqs.to_frame(name = 'typeFreqs')
    return df
    
    
    
    
    freqs_age = df[['age', 'utterance']].groupby('age').agg('count')
    freqs_age.add_suffix('_Count').reset_index()
    return freqs_age

#ngrams