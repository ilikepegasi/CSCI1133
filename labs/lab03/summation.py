
def print_endsum(val):
    sval = str(val)
    print(int(sval[0]) + int(sval[-1]))
def return_endsum(val):
    sval = str(val)
    return(int(sval[0]) + int(sval[-1]))

print_endsum(125) + print_endsum(907)
return_endsum(125) + print_endsum(907)
return_endsum(125) + return_endsum(907)
return_endsum(print_endsum(53208))
print_endsum(return_endsum(53208))

