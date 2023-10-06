
def anonymize(username, domain):
    '''
    Purpose: Anonymizes the username and appends it to the domain
    Parameters:
        username - (string) The username to be anonymized
        domain - (string) The domain name to be appended to the username
    Return Value: (string) The anonymized username appended to the username
        
    '''
    anonymized = username[0] + "*"*5 + username[-1] + domain

    return(anonymized)

def main():
    print(anonymize("andy.exley", "@gmail.com"))

if __name__ == "__main__":
    main()