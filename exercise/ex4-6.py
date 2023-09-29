def get_matching(word1, word2):
    sameLetters = ""
    for i in range(0, len(word1)):
        if word1[i] == word2[i]:
            sameLetters += word1[i]
    return sameLetters

print(get_matching('stack', 'stock'))
