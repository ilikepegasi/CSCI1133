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
    Purpose: 
        Finds all combinations of two inputted lists of strings that have a 
        length equivalent to an inputted length value
    Parameter(s):
        first_names: the list of possible first names (list)
        last_names: the list of possible last names (list)
        length: the desired length for the strings in the returned list (int)
    Return Value:
        A list of all the strings from the possible combinations of input values with length 
        equivalent to the inputted length value (list)
    '''

    valid_names = []
    for first_name in first_names:
        for last_name in last_names:
            possible_name = f"{first_name} {last_name}"
            if len(possible_name) == length:
                valid_names.append(possible_name)
    return valid_names

def change_key(notes, up):
    '''
    Purpose:
        Converts the key of the inputted user notes by incrementing or decrements the notes by the 
        distance specified by another inputted value
    Parameter(s):
        notes: the inputted notes to be key shifted (list)
        up: the amount of steps to take on the scale for notes (int)
    Return Value:
        The user inputted notes key shifted by as many steps they specified on the scale (list)
    '''

    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    shifted_notes = []
    for i in range(0, len(notes)):
        shifted_notes.append(scale[(scale.index(notes[i]) + up) % 12])
    return shifted_notes
