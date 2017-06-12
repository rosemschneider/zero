##script for pulling out text from yang clean corpus

#read in the text file
def find_sents(fname, substr):
    #pull out the lines corresponding to the word you're querying
    import re
    word_occur = []
    pattern = re.compile(substr, re.IGNORECASE)
    with open (fname, 'rt', encoding = 'latin1') as in_file:
        for linenum, line in enumerate(in_file):
            if pattern.search(line) !=None:
                word_occur.append((line.rstrip('\n')))
     
    #save it to text
    filename = ('parse_tag_out/' + substr + '_search.txt')
    
    import numpy
    numpy.savetxt(filename, word_occur, fmt = '%s')
    

def parse_sents(fname, substr):
    find_sents(fname, substr)
    
    parsename = ('parse_tag_out/' + substr + '_parse.txt')
    
    #make some variables to make running os.system easier
    cmd = ('parse_tag/parse/./lexparser.sh ' + 'parse_tag_out/' + substr + '_search.txt'
           + ' > ' + parsename + ' 2>&1')
    import os
    #actually run command - this is running the parser in the command line
    #this is also saving the results of the parse as a txt file in the cwd
    os.system(cmd)
    
def tag_sents(fname, substr): 
    find_sents(fname, substr)
    
    filename = (' ../../parse_tag_out/' + substr + '_search.txt')
    
    tagname = (' ../../parse_tag_out/' + substr + '_tag.txt')
    
    import os
    os.chdir('/Users/rschneid/Documents/Projects/zero/parse_tag/tag')
    cmd = ('./stanford-postagger.sh models/english-left3words-distsim.tagger' +
           filename + ' > ' + tagname + ' 2>&1')
    
    import os
    os.system(cmd)
 
    
        
    
    
        
 
              
    
    
                
     
     
    
    
    
                     