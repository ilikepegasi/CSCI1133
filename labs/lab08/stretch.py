def repeats_first_letter(user_input):
    if user_input.find(user_input[0], 1) != -1:
        return True
    return False

def is_palindrome(user_input):
    user_input = user_input.strip().lower()
    incidentals = ",.:?'\" "
    for char in incidentals:
        user_input = user_input.replace(char, "")
    if user_input[::-1] == user_input:
        return True
    return False

def find_first_letter_repeaters():
    repeats_first_letter_list = []
    user_input = input()
    while user_input != "":
        if repeats_first_letter(user_input):
            repeats_first_letter_list.append(user_input)
        user_input = input()
    print(repeats_first_letter_list)

def main():
    print(is_palindrome('Telat'))
    print(is_palindrome("Madam I'm Adam"))

if __name__ == "__main__":
    main()