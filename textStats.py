def corpusClean(txt):
    clean = txt.replace('\n', '')
    return clean

def getTokens(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a list of tokenized words.
    Symbols are separated out, and upper case is lowered.
    """
    corpusClean(txt)
    sym = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    new = txt.lower()
    for s in sym :
        new = new.replace(s, " "+s+" ")
        new = new.rstrip('\n') #for childes input
    return new.split()


def getTypeFreq(txt):
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
    """Takes a piece of text (a single string) as the argument.
    Returns a alphabetically sorted list of unique word types.
    """ 
    # [2] Complete this function. YOUR CODE BELOW. 
    types = dict(getTypeFreq(txt))
    return list(sorted(types.keys()))


def getXLengthWords(wtypes, x):
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
    """Takes a word frequency dictionary and integer x as arguments.
    Returns a sorted list of words that are at least x in frequency.
    """
    # [4] Complete this function. YOUR CODE BELOW.
    new = []
    for k, v in freqdi.items():
        if(v >= x):
            new.append(k)
    return new


def foxDemo():
    "A void function that demonstrates how the functions are used."
    foxtoks = getTokens(fox)      # Function-internal objects:
    foxtypes = getTypes(fox)      #   not accessible from IDLE shell!
    foxfreq = getTypeFreq(fox)    # You can however retrace the steps 
                                  #   to re-create these objects. 
    print('There are', len(foxtoks), 'word tokens in fox.')
    print('There are', len(foxtypes), 'unique word types in fox.')
    print('The word "freezy" occurs', foxfreq['freezy'], 'times.')

    len6 = getXLengthWords(foxtypes, 6)
    freq3 = getXFreqWords(foxfreq, 3)

    print('Words that are at least 6-characters long: ')
    for w in len6 :
        print(' ', "'"+w+"'", 'has', len(w), 'chars.')

    print('Words with 3 or higher frequency: ')
    for w in freq3 :
        print(' ', "'"+w+"'", 'occurs', foxfreq[w], 'times.')


def getWord2Grams(wds):
    wds = corpusClean(wds)
    wds = wds.split(' ')
    output = []
    for i in range(len(wds)-2+1):
        output.append(wds[i:i+2])
    tuples = [tuple(l) for l in output]    
    return tuples

def getWord3Grams(wds):
    wds = corpusClean(wds)
    wds = wds.split(' ')
    output = ()
    for i in range(len(wds)-3+1):
        output.append(wds[i:i+3])
    tuples = [tuple(l) for l in output]
    return tuples


def getFreq(li):
    "Takes a list as input, returns a dictionary of frequency count."
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] += 1
    return di


##To do after lunch
    #ignore special characters
    #substring-specific bigrams
    