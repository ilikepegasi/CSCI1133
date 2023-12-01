
def find_vowel(word):
    vowels = "aieou"
    for i, letter in enumerate(word):
        for vowel in vowels:
            if letter in vowels:
                return i

def capitalize(word, flag):
    if flag:
        return word[0].upper() + word[1:]
    return word

def igpay(sentence):
    words = sentence.split()
    pigged_words = []
    punctuation = "'\".,:;?!"
    for i, word in enumerate(words):
        word_punctuation = ""
        upper_flag = False
        if word[0] == word[0].upper():
            upper_flag = True
        word = word.lower()
        for char in word:
            if char in punctuation:
                word_punctuation = char
                word = word.replace(char, "")
        first_vowel_index = find_vowel(word)
        if first_vowel_index == None:
            pigged_words.append(capitalize(word, upper_flag) + "ay")
        else: 
            word_slice = word[0:first_vowel_index]
            if word_slice != "":
                word = capitalize(word[first_vowel_index:len(word)], upper_flag) + word_slice + "ay" + word_punctuation
                pigged_words.append(word)
            else:
                word = capitalize(word, upper_flag) + "way" + word_punctuation
                pigged_words.append(word)
    return " ".join(pigged_words)

def main():
    print(igpay('Synthesis has a lot of leading consonants. Rhythm has no vowels? By. '))

if __name__ == "__main__":
    main()
