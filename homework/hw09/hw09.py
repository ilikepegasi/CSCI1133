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

def create_list(fname):
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read().split()        
        for i, line in enumerate(text):
            text[i] = line.split(",")
    return text

def more_popular(fname, target):
    #TODO add docstring
    text = create_list(fname)
    for i, name_pair in enumerate(text):
        if target == name_pair[0]:
            popularity = int(text[i][1])
    popular_names = []
    for name_pair in text:
        if int(name_pair[1]) > popularity:
            popular_names.append(name_pair[0])
    return popular_names

def combine_names(fname1, fname2, outfile):
    text1 = create_list(fname1)
    text2 = create_list(fname2)
    i, j = 0, 0
    text3 = []
    while i < len(text1) and j < len(text2):
        if text1[i][0] == text2[j][0]:
            text3.append([text1[i], int(text1[i][1]) + int(text2[i][1])])
            i += 1
            j += 1
        elif text1[i][0] > text2[j][0]:
            text3.append(text1[1])
            i += 1
        elif text2[j][0] > text1[i][0]:
            text3.append(text2[j])
            j += 1
        while i < len(text1):
            i += 1

