import random

#DO NOT EDIT THE decrypt FUNCTION
#You're not required to understand how this works, but I've provided
#documentation to give you a general idea.
def decrypt(data, password):
    '''
    Purpose:
      Check whether the password is correct for a given encrypted
      file, and print out the decrypted contents if it is.
    Input Parameter(s):
      data is a string, representing the contents of an encrypted file.
      password is a four letter lowercase string, representing the password
      used to encrypt/decrypt the file contents.
    Return Value:
      Returns True if the password is correct and the file contents
      were printed.  Returns False and prints nothing otherwise.
    '''

    total = 0
    for ltr in password:
        total += ord(ltr)
        total *= 123
    encoded_pwd = pow(total,2011,547120141)
    
    data = data.split('\n')
    if encoded_pwd == int(data[0]):
        i = 0
        out_msg = ''
        for ltr in data[1]:
            out_msg += chr((ord(ltr)-ord(password[i]))%28 +97)
            i = (i+1)%len(password)
        out_msg = out_msg.replace('{',' ').replace('|','.')
        print(out_msg)
        return True
    return False


# Problem A: Spooky Numbers
def spooky(val):
    '''
    Purpose:
        Determines whether the input value is a spooky number, defined by when it is not divisible 
        by a number between 10 and 31 inclusive
    Input Parameter(s):
        val: the value to be determined whether it is a spooky number (int)
    Return Value:
        Whether the input value is a spooky number (bool)
    '''
    for i in range(10, 32):
        if (val % i) == 0:
            return False
    return True

# Problem B: Simulating a Sequence of Events
def five_heads():
    '''
    Purpose:
        Simulates coin flips until five in a row are found, counting how many attempts are taken before the five in a row happens
    Parameter(s):
        None
    Return Value:
        The amount of resets before five in a row heads happened (int)
    '''
    count = 0
    retries = 0
    while count <= 5:
        if random.randint(0, 1) == 0:
            count += 1
        else:
            count = 0
            retries += 1
    return retries

# Problem C: Estimating Sequence Probabilities
def average_five(n):
    '''
    Purpose:
        Finds the average amount of tries it takes to get five heads in a row flipping a coin
    Parameter(s):
        n: the amount of iterations the program will complete to find the average value
    Return Value:
        The average amount of tries it takes to get five heads in a row using the user inputed iteration amount
    '''
    total_tries = 0
    for i in range(0, n):
        total_tries += five_heads()
    return (total_tries / n)

# Problem D: Brute Force Password Cracking
def find_password(filename):
    '''
    Purpose:
      Given an encrypted file, tries every possible four letter lowercase
      password for that file until one works, and then returns the password.
    Input Parameter(s):
      filename is a string representing the name of the encrypted file.
      The file must be in the same folder as this script.
    Return Value:
      Returns the password that successfully decrypts the given file
    '''
    fp = open(filename)
    data = fp.read()
    fp.close()
    password = "aaaa"
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter1 in alphabet:
        for letter2 in alphabet:
            for letter3 in alphabet:
                for letter4 in alphabet:
                    password = letter1 + letter2 + letter3 + letter4
                    if decrypt(data, password):
                        return password
    return False


if __name__ == '__main__':
    print(spooky(35)) #Should output True
    print(spooky(31)) #Should output False
    print(spooky(1517)) #Should output True
    print(spooky(323)) #Should output False
    print(spooky(32)) #Should output False
    print(spooky(71)) #Should Output True


if __name__ == "__main__":
    print(average_five(10000))
if __name__ == '__main__':
    print(find_password('encrypted1.txt')) #Should output ford
    print()
    print(find_password('encrypted2.txt')) #Should output glad
    print()
    print(find_password('invalid.txt')) #Should output False
    print()