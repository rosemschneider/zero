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

os.chdir('/Users/rschneid/Documents/Projects/zero')

import textSearch
import textStats
import analysis

#a function for reading in dfs
def readCSV(fname):
    df = pd.DataFrame.from_csv(fname)
    return df

df_1 = readCSV('zero_search1.csv')

def filterDF(df, column, substr):
    filtered = []
    # for row in data frame,
    for row in df[column]:
        # for each key and value in the row,
        for key, value in row.items():
            if(type(substr) == tuple):
                for s in substr:
                    if s == str(key):
                        new_dict = dict()
                        new_dict[key] = value
                        filtered.append(new_dict)
            else:
                # if the key matches desired substring,
                if substr == str(key):
                    # set the key in the new dictionary equal to the
                    # value associated with the matching key
                    new_dict = dict()
                    new_dict[key] = value                       
                    # append the new dictionary object to a list
                    # called "filtered"
                    filtered.append(new_dict)
#                    print(filtered)
    return filtered 

#frequencies by age
def freqsByAge(df, substr):
    """This is a function to return the number of utterances a given word 
    by age."""
    empty_col = []   
    for row in df['utterance']:
        empty_col.append(textStats.getTypeFreq(row))   
    freqs = pd.Series(empty_col)
    #need to convert series to df to append
    freqs = freqs.to_frame(name = 'typeFreqs')
    df['typeFreqs'] = freqs['typeFreqs']
    
    #now get the actual values for only the substr you're interested in
    filtered_freqs = filterDF(df, 'typeFreqs', substr)
    #get the get the values
    vals = []
    for entry in filtered_freqs:
        for value in entry.items():
            vals.append(value[1])
    #now that we have the values, append them to the df
    num = pd.Series(vals)
    num = num.to_frame(name = 'searchVals')
    #add to the actual df
    df['searchVals'] = num['searchVals']
    
    #finally, convert the age to numbers, drop the none
    tmp_df = df
    tmp_df = tmp_df[(tmp_df['age'] != '[None]')]
    df = tmp_df
    for age in df['age']:
        age = int(age)
    return df    
    

##now I need to make a graph based on frequencies by age


 
    
    
    
    
    freqs_age = df[['age', 'utterance']].groupby('age').agg('count')
    freqs_age.add_suffix('_Count').reset_index()
    return freqs_age

#ngrams