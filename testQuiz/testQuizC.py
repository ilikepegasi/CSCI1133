def lower(word):
    out = ''
    for ch in word:
        if ord('A') <= ord(ch) and ord(ch) <= ord('Z'):
            new_ch = chr(ord(ch) + 32)
            out += new_ch
        else:
            out += ch
    return out

fname = 'out.txt'
file_in = open(fname)

count = 0
for line in file_in:
    count += len(line)
print(count)
file_in.close()


def rem_first(fname):
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read()
    text = text.split("\n")
    for i, line in enumerate(text):
        text[i] = line[1:]
    text = "\n".join(text)
    new_name = "rem_" + fname
    with open(new_name, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(text)

