def file_data(fname):
    fp = open(fname, "r")
    first_line_characters = len(fp.readline(-1))
    fp.close()
    fp = open(fname)
    total_characters = len(fp.read())
    fp.close()
    fp = open(fname)
    lines = len(fp.read().split("\n"))
    fp.close()
    fp = open(fname)
    words = len(fp.read().split())
    fp.close()
    return [first_line_characters, total_characters, lines, words]


file_data("footloose.txt")
