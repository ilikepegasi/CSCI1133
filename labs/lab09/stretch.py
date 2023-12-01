import random as rand

def make_data(fname):
    with open(fname, "x") as file_pointer:
        synthetic_data = ""
        for i in range(-1000, 1001):
            synthetic_data += str(rand.randint(-1000,1000)) + "," + str(rand.randint(-1000,1000)) + "\n"
        file_pointer.write(synthetic_data)


def read_data(fname):
    try:
        with open(fname, "r") as file_pointer:
            text = file_pointer.read()
        text = text.split()
        for i, line in enumerate(text):
            text[i] = line.split(",")
        max_num = -1000
        min_num = 1000
        for i, pair in enumerate(text):
            n1 = int(pair[0])
            n2 = int(pair[1])
            if n1 < min_num:
                min_num = n1
            if n2 < min_num:
                min_num = n2
            if n1 > max_num:
                max_num = n1
            if n2 > max_num:
                max_num = n2
        print(min_num, max_num)
    except FileNotFoundError:
        print("you are a bad user")

read_data("testFiles/syntheticData.txt")