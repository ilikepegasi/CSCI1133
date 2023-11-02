def function_names(fname):
    #TODO add docstring
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read()
        names = []
        def_index = text.find("def ")
        while def_index != -1:
            paren_index = text.find("(", def_index)
            names.append(text[def_index + 4:paren_index])
            def_index = text.find("def ", paren_index)
        return names



def more_popular(fname, target):
    #TODO add docstring
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read().split()
        for i, line in enumerate(text):
            text[i] = line.split(",")
        print(text)

