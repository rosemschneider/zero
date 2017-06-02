##script for pulling out text from yang clean corpus

#read in the text file

def find_sents():
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
   
    filename = (substr + '_search.txt')
    
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')
    #to do:
        #figure out subprocess so I can launch the parser from here
        
    
    
        
 
              
    
    
                
     
     
    
    
    
                     