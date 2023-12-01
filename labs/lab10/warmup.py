def word_freq(fname):
    with open(fname) as fp:
        text = fp.read()
    text = text.split("\n")
    counts = {}
    for line in text:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts

def main():
    print(word_freq("testFiles/sample1.txt"))

if __name__ == "__main__":
    main()

