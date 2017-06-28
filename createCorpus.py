"""
This is a script to read in corpora and output to csv for future analysis. 
Comes with two functions - can be used to import only utterances containing [x] words, 
Or can be used to import all utterances. 

NB still to be done - metadata about context and sex of child, if possible. Also, 
need to get participants so I can do this separately for input and production.
"""

import os
import glob
import re
import pandas as pd
import nltk
from nltk.corpus.reader import CHILDESCorpusReader

os.chdir('/Users/rschneid/Documents/Projects/zero')

import textSearch
import textStats

corpus_root = nltk.data.find('corpora/childes/data-xml/english')

#Exact matches for numbers - zero is included in each grouping for ease of comparison
numbers_to_ten = '\\bzero\\b|\\bthree\\b|\\bfour\\b|\\bfive\\b|\\bsix\\b|\\bseven\\b|\\beight\\b|\\bnine\\b|\\bten\\b'

numbers_teens = '\\bzero\\b|\\beleven\\b|\\btwelve\\b|\\bthirteen\\b|\\bfourteen\\b|\\bfifteen\\b|\\bsixteen\\b|\\bseventeen\\b|\\beighteen\\b|\\bnineteen\\b'

numbers_decades = '\\bzero\\b|\\btwenty\\b|\\bthirty\\b|\\bforty\\b|\\bfifty\\b|\\bsixty\\b|\\bseventy\\b|\\beighty\\b|\\bninety\\b|\\bhundred\\b'

numbers_large = '\\bzero\\b|\\bthousand\\b|\\bmillion\\b|\\bbillion\\b|\\btrillion\\b'

zero = '\\bzero\\b'

#list of corpora over which to iterate
corpus = ['Bates', 'Bernstein', 'Bliss', 'Bloom70', 'Bloom73',
          'Bohannon', 'Braunwald', 'Brent', 'Brown', 
          'Clark', 'Cornell', 'Cruttenden', 'Davis', 'Demetras1', 
          'Fletcher', 'Forrester', 'Garvey', 'Gathburn', 'Gathercole', 
          'Gleason', 'HSLLD', 'Haggerty', 'Hall', 'Higginson', 'Howe',
          'Korman', 'Kuczaj', 'Lara', 'MacWhinney', 'Manchester', 'McMillan', 
          'Morisset', 'MPI-EVA-Manchester', 'NH', 'Nelson', 'NewEngland','Normal', 'Post','Providence',
          'Rollins', 'Sachs', 'Sawyer', 'Snow','Soderstrom', 'Sprott',
          'Suppes', 'Tardif', 'Thomas', 'Tommerdahl', 'Valian', 'VanHouten',
          'VanKleeck', 'Warren', 'Weist', 'Wells']

corpus = ['Clark', 'Cornell', 'Cruttenden', 'Davis', 'Demetras1', 
          'Fletcher', 'Forrester', 'Garvey', 'Gathburn', 'Gathercole', 
          'Gleason', 'HSLLD', 'Haggerty', 'Hall', 'Higginson', 'Howe',
          'Korman', 'Kuczaj', 'Lara', 'MacWhinney', 'Manchester', 'McMillan', 
          'Morisset', 'MPI-EVA-Manchester', 'NH', 'Nelson', 'NewEngland','Normal', 'Post','Providence',
          'Rollins', 'Sachs', 'Sawyer', 'Snow','Soderstrom', 'Sprott',
          'Suppes', 'Tardif', 'Thomas', 'Tommerdahl', 'Valian', 'VanHouten',
          'VanKleeck', 'Warren', 'Weist', 'Wells']

def createCSV_numbers(corpora, numbers, speaker, fname):
    """This is a function that takes a list of corpora names (already defined),
    and writes output to csv if utterance is in query list. 
    Query list must be written in regex.
    
    Speaker must equal 'CHI' for output, or 'ALL' for input.
    
    fname must be a str (e.g., 'zero_search.csv')"""
    for corp in corpora: #for each individual corpus
      string = corp + '/.*.xml'
      subcorp = CHILDESCorpusReader(corpus_root, string)
      sents = []
      age_array = []
      mlu = []
      fileid = []
      for file in subcorp.fileids(): #for each file in corpus
                                
          #get the participants in this file
          participants = list(subcorp.participants(file))
          participants = participants[0].keys()
          participants = list(participants)
          
          #determine whether you're pulling input or output
          if (speaker == 'ALL'):
              for person in participants:
                  if(person == 'CHI'): #only input, not output
                      participants.remove(person)
          else:
              participants = 'CHI'
              
          #for each utterance in the corpus    
          for words in subcorp.sents(fileids = file, speaker = participants):
              tmp_utterance = str(words)
              #only pull out the utterances containing words you care about
              pattern = re.compile(numbers, re.IGNORECASE)
              if pattern.search(tmp_utterance) !=None:
                utterance = str(words)  
                sents.append(textStats.corpusClean(utterance)) 
                fileid.append(file)
                #convert the age
                age_list = subcorp.age(file)
                if(str(age_list) != '[None]'): #some of the ages not listed
                    age = age_list[0]
                    age = subcorp.convert_age(age)
                else:
                    age = subcorp.age(file)
                age_array.append(age)
                mlu.append(subcorp.MLU(file))
      
      #pull all of the data together into something df-like         
      corpus = zip(fileid, age_array, mlu, sents)
      corpus = list(corpus)
      #now we need to make that corpus a df
      df_corpus = pd.DataFrame(corpus)
      #now write that sucker to csv)
      with open(fname, 'a') as f: 
          df_corpus.to_csv(f, header=f)
      #now clear memory to make sure python doesn't freak
      string = ""
      subcorp = ""
      sents = []
      age = []
      mlu = []
      fileid = []
      
#NOTE: This general function is out of date - need to update to reflect the above      
#def createCSV(corpora):
#    """This is the generic corpus writer. This will output every line of a corpus to 
#    a csv."""
#  for c in corpora: #for each individual corpus
#      string = c + '/.*.xml'
#      subcorp = CHILDESCorpusReader(corpus_root, string)
#      tmp_sents = []
#      sents = []
#      age = []
#      mlu = []
#      fileid = []
#      for i in subcorp.fileids():
#          for j in subcorp.sents(fileids = i, speaker = 'ALL'):
#            utterance = str(j)  
#            sents.append(textStats.corpusClean(utterance)) 
#            fileid.append(i)
#            age.append(str(subcorp.age(i)))
#            mlu.append(subcorp.MLU(i))
#            tmp_sents = []
#      corpus = zip(fileid, age, mlu, sents)
#      corpus = list(corpus)
#      #now we need to make that corpus a df
#      df_corpus = pd.DataFrame(corpus, columns = ['fileid', 'age', 'mlu', 'sentences'])
#      #now write that sucker to csv)
#      with open('test.csv', 'a') as f:
#          df_corpus.to_csv(f, header=f)
#      #now clear memory to make sure python doesn't freak
#      string = ""
#      subcorp = ""
#      sents = []
#      age = []
#      mlu = []
#      fileid = []       
