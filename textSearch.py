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
    pattern = re.compile('zero', re.IGNORECASE)
    with open ('input.txt', 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
    
    import numpy
    numpy.savetxt('test1.txt', word_occur, fmt = '%s')
        
 
              
    
    
                
     
     
    
    
    
                     