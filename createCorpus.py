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

os.chdir('/Users/roseschneider/Documents/Projects/zero')

import textSearch
import textStats

corpus_root = nltk.data.find('corpora/childes/data-xml/english')

brown = CHILDESCorpusReader(corpus_root, 'Brown/.*.xml')
sarah = [f for f in brown.fileids() if f[6:11] == 'Sarah']

numbers = '\\bzero\\b'|\\bfive\\b|\\bsix\\b|\\bseven\\b|\\beight\\b|\\bnine\\b|\\bten\\b\\beleven\\b|\\btwelve\\b|\\bthirteen\\b|\\bfourteen\\b|\\bfifteen\\b|\\bsixteen\\b|\\bseventeen\\b|\\beighteen\\b|\\bnineteen\\b\\btwenty\\b|\\bthirty\\b|\\bforty\\b|\\bfifty\\b|\\bsixty\\b|\\bseventy\\b|\\beighty\\b|\\bninety\\b\\bhundred\\b|\\bthousand\\b|\\bmillion\\b|\\bbillion\\b|\\btrillion\\b'
corpus = ['Bates' ,'Gathercole', 'Peters', 'Belfast',			
             'Gillam',	 'Post', 'Bernstein',	'Gleason', 'Providence', 
             'Bliss',	'HSLLD', 'Rollins', 'Bloom70', 'Haggerty', 'Sachs',
             'Bloom73', 'Hall', 'Sawyer', 'Bohannon', 'Higginson', 'Snow',
             'Braunwald', 'Howe', 'Soderstrom', 'Brent', 	'Korman', 'Sprott',
             'Brown',	'Kuczaj', 'Suppes', 'Clark', 'Lara', 'Tardif', 
             'Cornell', 'MPI-EVA-Manchester', 'Thomas', 
             'Cruttenden', 'MacWhinney', 'Tommerdahl',
             'Davis',	'Manchester',	'Valian', 'Demetras1',	 'McMillan',		
             'VanHouten' 'ErvinTripp', 'Morisset', 'VanKleeck',
             'Fletcher', 'NH', 'Warren', 'Forrester', 'Nelson'	, 'Weist',
             'Garvey', 'NewEngland', 'Wells', 'Gathburn', 'Normal']


def createCSV_numbers(corpora, numbers):
    """This is a function that takes a list of corpora names (already defined),
    and writes output to csv if utterance is in query list. 
    Query list must be written in regex.
    
    Make sure you have an empty csv ready before you run this, 
    change the csv name if you need to."""
    for corp in corpora: #for each individual corpus
      string = corp + '/.*.xml'
      subcorp = CHILDESCorpusReader(corpus_root, string)
      sents = []
      age_array = []
      mlu = []
      fileid = []
      for file in subcorp.fileids():
          #this is getting the participants - currently only for input
          #need to modify this to accept user input to designate production
          participants = list(subcorp.participants(file))
          participants = participants[0].keys()
          participants = list(participants)
          for person in participants:
              if(person == 'CHI'): #only input, not output
                  participants.remove(person)   
          for words in subcorp.sents(fileids = file, speaker = participants):
              tmp_utterance = str(words)
              pattern = re.compile(numbers, re.IGNORECASE) #only pull out utterances with numbers
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
                    age = subcorp.age(i)
                age_array.append(age)
                mlu.append(subcorp.MLU(i))
      corpus = zip(fileid, age_array, mlu, sents)
      corpus = list(corpus)
      #now we need to make that corpus a df
      df_corpus = pd.DataFrame(corpus)
      #now write that sucker to csv)
      with open('zero_search1.csv', 'a') as f: #to-do - allow user to specify filename
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
