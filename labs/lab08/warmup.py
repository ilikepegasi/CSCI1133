a = "mississippi"
print(a.count("s"))
print(a.replace("iss", "ax"))
print(a.index("p"))
def foo(istring):
    p = '0123456789'
    os = ''
    for ch in istring:
        if ch not in p:
            os += ch
    return os
    # For every time a character in istring is not digit 0-9, add it to os and return it
print(foo("49w58ddg(7##"))
def foo2(istring):
    p = '0123456789'
    os = ''
    for i in range(len(istring)):
        if istring[i] not in p:
            os += istring[i]
    return os
print(foo("49w58ddg(7##"))
