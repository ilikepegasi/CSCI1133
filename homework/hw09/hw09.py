def function_names(fname):
    #TODO add docstring
    try:
        with open(fname, "r", encoding="utf-8") as file_pointer:
            text = file_pointer.read()
            names = []
            def_index = text.find("def ")
            while def_index != -1:
                paren_index = text.find("(", def_index)
                names.append(text[def_index + 4:paren_index])
                def_index = text.find("def ", paren_index)
            return names
    except FileNotFoundError:
        print("Invalid filename")

def more_popular(fname, target):
    #TODO add docstring
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read().split()
        for i, line in enumerate(text):
            text[i] = line.split(",")
            text[i][1] = int(text[i][1])
            if text[i][0] == target:
                index = i
        popularity = text[index][1]
        popular_names = []
        for name_pair in text:
            if name_pair[1] > popularity:
                popular_names.append(name_pair[0])
        return popular_names

def combine_names(fname1, fname2, outfile):
    print()