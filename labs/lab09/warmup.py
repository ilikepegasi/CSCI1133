def wordcount(fname):
    try:
        with open(fname, "r", encoding="utf-8") as file_pointer:
            text = file_pointer.read()
            return len(text.split())
    except FileNotFoundError:
        print("File not found")
        return -1


print(wordcount("testFiles/testText.txt"))