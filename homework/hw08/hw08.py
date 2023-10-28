def complement(dna_string):
    '''
    '''
    dna_string = dna_string.replace("A", "t")
    dna_string = dna_string.replace("T", "a")
    dna_string = dna_string.replace("G", "c")
    dna_string = dna_string.replace("C", "g")
    return dna_string.upper()

def open_word_file():
    '''
    Purpose: Returns the string containing the words from the file words.txt
    Parameter(s):
        None
    Return Value:
        (str) The plain text of the file words.txt
    '''
    fp = open('words.txt')
    common_words = fp.read().split()
    fp.close()
    return common_words

def correct_word(text):
    '''
    Purpose: Corrects a single incorrect letter in a given word
    Parameter(s):
        text: (str) A string of lowercase letters representing the
        English word we want to correct.
    Return Value:
        (str) A word that's at most one letter away from the given
        text, if one can be found in words.txt.  Or '???' if not.
    '''
    common_words = open_word_file()
    if common_words.count(text) != 0:
        return text
    for word in common_words:
        if len(word) == len(text):
            shared_letters = 0
            for i, letter in enumerate(text):
                if word[i] == letter:
                    shared_letters += 1
            if shared_letters >= (len(word) - 1):
                return word
    return "???"

def correct_all(sentence):
    '''
    Purpose:
        Corrects the spellings of each words in a sentence by checking similarity to the top 1000
        words in the English language. If none can be found, the word is replaced with ???.
        It assumes no capitalization other than for the first letter and no punctuation other 
        than a final period.
    Parameters:
        sentence: (str) the sentence to be spellchecked 
    Return Value: (str)
        The sentence with each of its words replaced with its closest equivalent in the top 1000 
        words of the English language. If no word is found, it is replaced with ???. The sentence 
        will be all lowercase, except for the first letter. It ends with one period. 
    '''
    sentence = sentence.replace(".", "")
    words = sentence.lower().split()
    words[0] = words[0].lower()
    for i, word in enumerate(words):
        words[i] = correct_word(word)
    words[0] = words[0][0].upper() + words[0][1:]
    words = " ".join(words)
    words += "."
    return words

def correct_word2(text):
    '''
    Purpose: 
        Finds a word in the top 1000 most common words in the 
        English language closest to your word
    Parameter(s):
        text: (str) A string of lowercase letters representing the
        English word we want to correct.
    Return Value:
        (str) A word found by making a single letter change to your given word, until your word matches
        if one can be found in words.txt. Or '???' if not.
    '''
    common_words = open_word_file()
    if common_words.count(text) != 0:
        return text
    for shared_letters_limit in range(1, len(text)):
        for word in common_words:
            if len(word) == len(text):
                shared_letters = 0
                for i, letter in enumerate(text):
                    if word[i] == letter:
                        shared_letters += 1
                if shared_letters >= (len(text) - shared_letters_limit):
                    return word
    return "???"

def correct_all2(sentence):
    sentence = sentence.replace(".", "")
    words = sentence.lower().split()
    words[0] = words[0].lower()
    for i, word in enumerate(words):
        words[i] = correct_word2(word)
    words[0] = words[0][0].upper() + words[0][1:]
    words = " ".join(words)
    words += "."
    return words


if __name__ == '__main__':
    #Should output You shall not pass.
    print(correct_all2('Bou shale net mass.'))

    #Should output ??? of these ??? ??? ???.
    print(correct_all2('Alll sf tgese wrds haev typos.'))
    
    #Should output More words not thus time they had be fixed.
    print(correct_all2('More sords bot thus timm whey cad be foxed.'))