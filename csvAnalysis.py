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
import matplotlib.pyplot as plt

os.chdir('/Users/rschneid/Documents/Projects/zero')

import textSearch
import textStats
import analysis

#a function for reading in dfs
def readCSV(fname):
    df = pd.DataFrame.from_csv(fname)
    return df

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

##Framework for generating graphs
#With zero input as example
zero_input = readCSV('data/zero_input.csv')

##For individual number words
#First, get the freqs by age
#group by age and aggregate by count
grouped = zero_input_freqs[['age', 'searchVals']].groupby('age').agg('count')

#I need to learn more about pandas, but this is my clunky way of getting
#values out of the grouped df

#ages need to be converted from strings to ints
age_int = []
ages = list(grouped.index)
for num in ages:
    num = int(num)
    age_int.append(num)

ages_int = np.asarray(age_int)    

values = grouped.values
values_int = []
for array in values:
    for number in array:
        values_int.append(number)
        
values_int = np.asarray(values_int)
    
zero_input_freqs = freqsByAge(zero_input, 'zero')
#Make a graph of the frequencies by age
plt.bar(ages_int, values_int)
plt.xlabel('Age (in months)', fontsize=12)
plt.ylabel('Frequency in input', fontsize=12)
plt.xticks(np.arange(min(ages_int), max(ages_int)+1, 10))
plt.title('Zero frequency by age - input')
 
    
##now I need to make a graph based on frequencies by age

#ngrams