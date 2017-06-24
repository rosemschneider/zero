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

os.chdir('Documents/Projects/zero')

import textSearch
import textStats

#a function for reading in dfs
def readCSV(fname):
    df = pd.DataFrame.from_csv(fname)
    return df

df = readCSV('zero_search1.csv')

#frequencies by age
freqs_age = df[['age', 'utterance']].groupby('age').agg('count')
freqs_age.add_suffix('_Count').reset_index()

#ngrams