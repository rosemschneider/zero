##script for pulling out text from yang clean corpus

#read in the text file
"""This is a support script with lots of beautiful functions for dealing
with and searching through text input."""
import re

def find_sents(fname, substr):
    """Function to find sentences that contain a single substring."""
    #pull out the lines corresponding to the word you're querying
    word_occur = []
    search = '\\b' + substr + '\\b'
    pattern = re.compile(search, re.IGNORECASE)
    with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
     
    #save it to text
    filename = ('parse_tag_out/' + substr + '_search.txt')
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')
  
    
###The following functions are just riffs on the find_sents() function.
def find_nums_to_ten(fname):
#    import re
     nums_to_ten = '\\bzero\\b|\\bone\\b|\\btwo\\b|\\bthree\\b|\\bfour\\b|\\bfive\\b|\\bsix\\b|\\bseven\\b|\\beight\\b|\\bnine\\b|\\bten\\b'
     word_occur = []
     pattern = re.compile(nums_to_ten, re.IGNORECASE)
     with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
                
     filename = ('parse_tag_out/' + 'num_to_ten' + '_search.txt')
    
     import numpy
     numpy.savetxt(filename, word_occur, fmt = '%s')
     
def find_nums_teens(fname):
#    import re
     nums_teens = '\\beleven\\b|\\btwelve\\b|\\bthirteen\\b|\\bfourteen\\b|\\bfifteen\\b|\\bsixteen\\b|\\bseventeen\\b|\\beighteen\\b|\\bnineteen\\b'
     
     
     word_occur = []
     pattern = re.compile(nums_teens, re.IGNORECASE)
     with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
                
     filename = ('parse_tag_out/' + 'nums_teens' + '_search.txt')
    
     import numpy
     numpy.savetxt(filename, word_occur, fmt = '%s')

def find_nums_decades(fname):
#    import re
     nums_decades = '\\btwenty\\b|\\bthirty\\b|\\bforty\\b|\\bfifty\\b|\\bsixty\\b|\\bseventy\\b|\\beighty\\b|\\bninety\\b'
     
     
     word_occur = []
     pattern = re.compile(nums_decades, re.IGNORECASE)
     with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
                
     filename = ('parse_tag_out/' + 'nums_decades' + '_search.txt')
    
     import numpy
     numpy.savetxt(filename, word_occur, fmt = '%s')      
     
def find_nums_large(fname):
#    import re
     nums_large = '\\bhundred\\b|\\bthousand\\b|\\bmillion\\b|\\bbillion\\b|\\btrillion\\b'
     
     
     word_occur = []
     pattern = re.compile(nums_large, re.IGNORECASE)
     with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
                
     filename = ('parse_tag_out/' + 'nums_large' + '_search.txt')
    
     import numpy
     numpy.savetxt(filename, word_occur, fmt = '%s')      

def parse_sents(fname, substr):
    """This is a function for parsing a text file with the Stanford NLP parser. 
    
    Note that you might have to change the paths here. You can do that with os."""
#    import re
    find_sents(fname, substr)
    
    parsename = ('parse_tag_out/' + substr + '_parse.txt')
    
    #make some variables to make running os.system easier
    cmd = ('parse_tag/parse/./lexparser.sh ' + 'parse_tag_out/' + substr + '_search.txt'
           + ' > ' + parsename + ' 2>&1')
    import os
    #actually run command - this is running the parser in the command line
    #this is also saving the results of the parse as a txt file in the cwd
    os.system(cmd)
    
def tag_sents(fname, outputName):
    """This is a function for tagging a text file with Stanford NLP taggers. 
    
    Note that you might have to change the paths here. You can do that with os."""
#    import re
#    find_sents(fname, substr)
    
    filename = (' ../../parse_tag_out/' + fname + '_search.txt')
    
    tagname = (' ../../parse_tag_out/tag/' + outputName + '_tag.txt')
    
    import os
#    os.chdir('/Users/rschneid/Documents/Projects/zero/parse_tag/tag')
    os.chdir('/Users/roseschneider/Documents/Projects/zero/parse_tag/tag')
    cmd = ('./stanford-postagger.sh models/english-left3words-distsim.tagger' +
           filename + ' > ' + tagname + ' 2>&1')
    
    os.system(cmd)
 
    
        
    
    
        
 
              
    
    
                
     
     
    
    
    
                     