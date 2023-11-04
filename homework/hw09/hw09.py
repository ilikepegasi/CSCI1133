def function_names(fname: str):
    '''
    Purpose:
        From an inputted file with python syntax, finds the names of each of the functions
    Parameter(s):
        fname (str): a string representing the filepath of the file in which to count the functions 
        of
    Return Value:
        (list[str]) A list of strings of each of the function names in the file
    '''
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
        return []

def create_list(fname: str):
    '''
    Purpose: 
        Creates a list of two lists from an inputted csv file with filepath fname,
        with the first column being the first value on each line of the csv and the second column 
        being the second value assuming the second value on each line of the csv is an integer
    Parameter(s):
        fname (str): a string representing the filepath of the inputted csv file
    Return Value (list[list[str, int]]):
        A list of two lists, first containing strings from the first entry on each line from an 
        inputted file with csv conventions, the second list containing intergers from that same
        file from the second entry
    '''
    with open(fname, "r", encoding="utf-8") as file_pointer:
        text = file_pointer.read().split()
        text_list = [[], []]
        for i, line in enumerate(text):
            text[i] = line.split(",")
            text_list[0].append(text[i][0])
            text_list[1].append(int(text[i][1]))
    return text_list

def more_popular(fname: str, target: str):
    '''
    Purpose:
        From an inputted csv file with two columns, one representing an event and the other 
        representing their frequency, finds a list of events that had a higher frequency than
        the inputted event, assuming the inputted event is included in the inputted file
    Parameter(s):
        fname (str): a string representing the filepath of the inputted csv file
        target (str): a string representing the event of which to find events that are more 
        popular than itself
    Return Value (list[str]): 
        A list of strings representing the names of events that were more frequent than the 
        inputted event in the inputted csv
    '''
    text = create_list(fname)
    target_index = text[0].index(target)
    target_num = text[1][target_index]
    popular_names = []
    for i, num in enumerate(text[1]):
        if num > target_num:
            popular_names.append(text[0][i])
    return popular_names

def combine_names(fname1: str, fname2: str, outfile: str):
    '''
    Purpose:
        Combines two inputted csv files with an event and frequency pair on each
        line and outputs to a new file, with each csv being alphabetically sorted based 
        on the event, when there is duplicate in the output files, the frequencies are
        added together and the events are consolidated into one entry
    Parameter(s):
        fname1 (str): a string representing the filepath of the first inputted csv file
        fname2 (str): a string representing the filepath of the second inputted csv file
        outfile (str): a string representing the filepath of output csv file
    Return Value (None): None
    '''
    text1 = create_list(fname1)
    text2 = create_list(fname2)
    i, j = 0, 0
    text3 = [[], []]
    while i < len(text1[0]) and j < len(text2[0]):
        if text1[0][i] in text3[0]:
            text3[1][text3[0].index(text1[0][i])] += text1[1][i]
            i += 1
        elif text2[0][j] in text3[0]:
            text3[1][text3[0].index(text1[0][i])] += text1[1][i]
            j += 1
        elif text1[0][i] < text2[0][j]:
            text3[0].append(text1[0][i])
            text3[1].append(text1[1][i])
            i += 1
        else:
            text3[0].append(text2[0][j])
            text3[1].append(text2[1][j])
            j += 1
    while i < len(text1[0]):
        text3[0].append(text1[0][i])
        text3[1].append(text1[1][i])
        i += 1
    while j < len(text2[0]):
        text3[0].append(text2[0][j])
        text3[1].append(text2[1][j])
        j += 1
    text_formatted = ""
    for i, name in enumerate(text3[0]):
        text_formatted += name + "," + str(text3[1][i]) + "\n"
    with open(outfile, "w", encoding="utf-8") as file_pointer:
        file_pointer.write(text_formatted)

if __name__ == "__main__":
    combine_names("testFiles/shortF.csv", "testFiles/shortM.csv", "testFiles/shortC_test.csv")
