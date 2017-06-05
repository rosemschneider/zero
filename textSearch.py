##script for pulling out text from yang clean corpus

#read in the text file

def find_sents():
    import os
    os.chdir('/Users/rschneid/Documents/Projects/zero/parse_tag')
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
    filename = ('../parse_tag_out/' + substr + '_search.txt')
    
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')
    

def parse_sents():
    #this is a function for finding and automatically parsing text using stanford nlp
    import os
    os.chdir('/Users/rschneid/Documents/Projects/zero/parse_tag')
    
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
    filename = ('../parse_tag_out/' + substr + '_search.txt')
    parsename = ('../parse_tag_out/' + substr + '_parse.txt')
    
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')
    
    #make some variables to make running os.system easier
    cmd = ('./lexparser.sh ' + filename + ' > ' + parsename + ' 2>&1')
    
    #actually run command - this is running the parser in the command line
    #this is also saving the results of the parse as a txt file in the cwd
    os.system(cmd)
    
def tag_sents(): 
    #function for using stanford tagger to generate tags
    import os
    #this dir needs to be fixed when I get things running more smoothly
    os.chdir('/Users/rschneid/Documents/Projects/zero/parse_tag')
    os.getcwd()

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
                
    #save output to text file
    filename = ('../parse_tag_out/' + substr + '_search.txt')
    tagname = ('../parse_tag_out/' + substr + '_tag.txt')
    
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')

    #create a command to make os.system happy 
    cmd = ('./stanford-postagger.sh models/english-left3words-distsim.tagger ' 
           + filename + ' > ' + tagname + ' 2>&1')
    
    #actually run the command
    os.system(cmd)
    
            
    
        
    
    
        
 
              
    
    
                
     
     
    
    
    
                     