###This is a script containing a lot of helpful functions for getting statistics
###about a corpus.
import re
def corpusClean(txt):
    """Function for removing special symbols from a corpus.
    
    Note that this removes 'x'. I need to fix this later, but right now
    I'm manually fixing these in the actual csv."""
    clean = txt.lower()
    clean = re.sub(r".\\n", " ", clean)
    clean = re.sub(r'[^A-Za-z0-9]+', ' ', clean)
    clean = re.sub(r"x\d*", " ", clean)
    return clean

def getTokens(txt):
#    import re
    """Takes a piece of text (a single string) as the argument.
    Returns a list of tokenized words.
    Symbols are separated out, and upper case is lowered.
    """
    corpusClean(txt)
    sym = "~!@#$%^&*()+=`{}[]|\\:;\"',./<>?"
    new = txt.lower()
    for s in sym :
        new = new.replace(s, " "+s+" ")
        new = new.rstrip('\n') #for childes input
    return new.split()


def getTypeFreq(txt):
#    import re
    """Takes a piece of text (a single string) as the argument.
    Returns a frequency count dictionary.
    KEY is a word, VALUE is its frequency count.
    """
    # [1] Complete this function. YOUR CODE BELOW.
    # Use getTokens().
    toks = getTokens(txt)
    counts = dict()
    for i in toks:
        counts[i] = counts.get(i, 0) + 1 
    freqs = sorted(counts.items(), key = lambda x:x[1], reverse = True)         
    return dict(freqs)


def getTypes(txt):
#    import re
    """Takes a piece of text (a single string) as the argument.
    Returns a alphabetically sorted list of unique word types.
    """ 
    # [2] Complete this function. YOUR CODE BELOW. 
    types = dict(getTypeFreq(txt))
    return list(sorted(types.keys()))


def getXLengthWords(wtypes, x):
#    import re
    """Takes a list of unique words (= word types) and integer x as
    arguments. Returns a sorted list of words whose length is at least x.
    """
    # [3] Complete this function. YOUR CODE BELOW.
    new = []
    for i in wtypes:
        if (len(i) >= x):
            new.append(i)
    return new


def getXFreqWords(freqdi, x):
#    import re
    """Takes a word frequency dictionary and integer x as arguments.
    Returns a sorted list of words that are at least x in frequency.
    """
    # [4] Complete this function. YOUR CODE BELOW.
    new = []
    for k, v in freqdi.items():
        if(v >= x):
            new.append(k)
    return new

def getWordnGrams(wds, n):
#    import re
    """Takes txt as input, and generates list of tuples of ngrams."""
#    wds = corpusClean(wds)
    wds = wds.split(' ')
    output = []
    for i in range(len(wds)-n+1):
        output.append(wds[i:i+n])
    tuples = [tuple(l) for l in output]    
    return tuples

def getFreq(li):
#    import re
    "Takes a list as input, returns a dictionary of frequency count."
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] += 1            
    return di

def sortFreqs(di):
#    import re
    """Takes a dictionary as input and sorts based on those values."""
    import operator
    di_sorted = sorted(di.items(), key = operator.itemgetter(1))
    return di_sorted

#pull out tags
def getSpec(di, substr):
#    import re
    """Takes a dictionary and string as input, returns a dictionary
    filtered down to entries containing that string."""
    new_dict = dict()
    for key, value in di.items():
        for s in substr:
            if s == str(key):
                new_dict[key] = value
    import operator
    new_dict = sorted(new_dict.items(), key = operator.itemgetter(1), reverse = True)    
    new = dict(new_dict)                
    return new

def getTags(di, substr):
#    import re
    """Takes a dictionary and string as input, returns a dictionary
    filtered down to entries containing that string."""
    new_dict = dict()
    for key, value in di.items():
        for s in substr:
            if s in str(key):
                new_dict[key] = value
    import operator
    new_dict = sorted(new_dict.items(), key = operator.itemgetter(1), reverse = True)    
    new = dict(new_dict)                
    return new    
    
    
#make histogram
def makeBar(di):
#    import re
    """Takes a dictionary as input and generates a bar plot."""
    import matplotlib.pyplot as plt
    plt.bar(range(len(di)),di.values(), align = 'center')
    plt.xticks(range(len(di)), di.keys(), rotation = 'vertical')
    plt.show()
    

    