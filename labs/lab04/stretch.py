
def choose_rb():
    choice = input("Choose Red or Blue: ")
    i = 0
    while (choice != "Red" or choice != "Blue") and i < 5:
        print(f'{choice} is not one of the valid options.')
        choice = input("Choose Red or Blue: ")
        i += 1

    return choice


if __name__ == "__main__":
    print(choose_rb())