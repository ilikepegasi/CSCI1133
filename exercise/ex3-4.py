def valid_street(name):
    return ((len(name) % 3 == 0) and ((name[0] == "r") or (name[0] == "R") or (name[0] == "g") or (name[0] == "G")))
if __name__ == '__main__':
    print(valid_street('gal'))
