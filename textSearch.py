##script for pulling out text from yang clean corpus

#read in the text file

def find_sents():
    import os
    os.chdir('/Users/rschneid/Documents/Projects/zero/stanford-parser-full-2016-10-31/')
    print("Please enter your substring")
    substr = input()
    print('Please enter your fileid')
    fname = input()
    type(fname)
                    
    #pull out the lines corresponding to the word you're querying
    import re
    word_occur = []
    pattern = re.compile(substr, re.IGNORECASE)
    with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
   
    
    #save it to text
    filename = (substr + '_search.txt')
    
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')
    

def parse_sents():
    #this is a function for finding and automatically parsing text using stanford nlp
    import os
    os.chdir('/Users/rschneid/Documents/Projects/zero/stanford-parser-full-2016-10-31/')
    
    #get user input
    print('Please enter your substring')
    substr = input()
    print('Please enter your fileid')
    fname = input()
    
    ##pull out the lines corresponding to the word you're querying
    import re
    word_occur = []
    pattern = re.compile(substr, re.IGNORECASE)
    with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
    
    #save it to text file
    filename = (substr + '_search.txt')
    parsename = (substr + '_parse.txt')
    
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')
    
    #make some variables to make running os.system easier
    cmd = ('./lexparser.sh ' + filename + ' > ' + parsename + ' 2>&1')
    
    os.system(cmd)
    
            
    
        
    
    
        
 
              
    
    
                
     
     
    
    
    
                     