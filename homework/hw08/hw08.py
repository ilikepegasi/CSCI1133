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
    sentence = sentence.replace(".", "")
    words = sentence.split()
    words[0] = words[0].lower()
    words[0] = correct_word(words[0])
    words[0] = words[0][0].upper() + words[0][1:]
    for i, word in enumerate(words):
        if i != 0:
            words[i] = correct_word(word)
    words = " ".join(words)
    words += "."
    return words

if __name__ == '__main__':
    #Should output You shall not pass.
    print(correct_all('Bou shale net mass.'))

    #Should output ??? of these ??? ??? ???.
    print(correct_all('Alll sf tgese wrds haev typos.'))
    
    #Should output More words not thus time they had be fixed.
    print(correct_all('More sords bot thus timm whey cad be foxed.'))
