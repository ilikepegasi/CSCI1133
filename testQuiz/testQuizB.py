def matrix_ops(data):
    data.append(1)
    data = data[:-1]
    data[0] = [2]
    data[0].append(3)
    for i in range(999):
        data.append(4)
        data = data[:-1]


grid = [[700, 800, 900]]
matrix_ops(grid)
def string_ops(data):
    data.lower()
    data.strip()
    for i in range(999):
        data = data.replace('a', 'A')
        data.replace('A', 'a')
    data = data[::-1]


grid = 'aAaaaAaaAabBBb    01010010  '
string_ops(grid)
st = "decade"
st = st.replace("a", "o")

def after_Re(word):
    index = word.find("Re:")
    if index != -1:
        return word[(index + 3):]
    return ""

def questions(phrase):
    words = phrase.split()
    for i in range(len(words)):
        word = words[i]
        word = word[1:]
        word = '?' + word
        words[i] = word
    return ' '.join(words)

print(questions('one two three four five six'))