def cross(u, v):
    '''
    Purpose:
        Returns the cross product of the two three dimensional vectors inputted as a new three dimensional vector
    Parameter(s): 
        u: first three dimensional vector, without units (list)
        v: second three dimensional vector, without units (list)
    Return Value:
        the three dimensional vector that is the cross product of the two inputted vectors (list)
    '''
    ru = u[1] * v[2] - u[2] * v[1]
    rx = u[2] * v[0] - u[0] * v[2]
    rv = u[0] * v[1] - u[1] * v[0]
    return [ru, rx, rv]


def all_names(first_names, last_names, length):
    '''
    '''
    possible_names = []
    valid_names = []
    for first_name in first_names:
        for last_name in last_names:
            possible_names.append([f"{first_name} {last_name}", len(first_name) + len(last_name) + 1])
            #The reason I set it up as a two dimensional list rather than calling len at evaluation is to be
            #able to include or remove the inserted space into the length count
    for full_name in possible_names:
        if full_name[1] == length:
            valid_names.append(full_name[0])
    return valid_names


print(all_names(['Sakshi', 'Hang', 'Leeje'], ['Singh', 'Yu', 'Jang'], 9))